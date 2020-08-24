import os
import time
import hashlib
import click

duplicated = 0
size = 0


@click.command()
@click.argument('dirs', type=click.Path(exists=True), nargs=-1, required=True)
@click.option('--chunk-size', '-c', type=click.IntRange(128, 2**32), default=4096, show_default=True,
              help='The size of every chunk of the file to read and update the checksum. '
                   'This value affects the Memory/CPU Usage as well as the progress speed.')
@click.option('--sleep-time', '-s', type=click.FloatRange(0, 120), default=0.001, show_default=True,
              help='The time to sleep (in seconds) while looping/iterating trow the files and calc the checksum. '
                   'This was made to prevent CPU Leak (100% Usage on some platforms).')
@click.option('--no-delete-empty', '-D', is_flag=True, help='Don\'t delete empty subdirectories.')
@click.option('--separate', '-S', is_flag=True, help='Delete duplicates in each directory separately.')
@click.option('--check-only', '-C', is_flag=True, help='Check only, Don\'t delete anything.')
@click.option('--recursive', '-R', is_flag=True, help='Check files and directories recursively.')
@click.option('--verbose', '-v', count=True, help='Output a diagnostic for every file processed.')
@click.option('--hash-type', '-h', default='sha1',
              type=click.Choice(['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'], case_sensitive=False),
              show_default=True, help='The hash type used to check the files\' checksum.')
def dupdel(dirs, chunk_size, sleep_time, no_delete_empty, separate, check_only, recursive, verbose, hash_type):
    """Check duplicated file and delete them using hash checksums."""
    global duplicated, size
    checksums_ = set()

    def get_checksum(file):
        h = hashlib.new(hash_type)
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                h.update(chunk)
        return h.hexdigest()

    def check_dir(working_dir):
        global duplicated, size
        checksums = set() if separate else checksums_
        listdir = os.listdir(working_dir)
        # Just wanna sort files first, because a want to keep top-level duplicated
        # files undeleted, and delete the inner duplications!
        listdir.sort(key=lambda x: (os.path.isdir(os.path.join(working_dir, x)), x))
        for name in listdir:
            path = os.path.join(working_dir, name)
            if os.path.isfile(path):
                checksum = get_checksum(path)
                if checksum in checksums:
                    duplicated += 1
                    size += os.path.getsize(path)  # TODO: PermissionError
                    if not check_only:
                        try:
                            os.remove(path)
                            if verbose >= 1:
                                click.echo('[-] duplicated file deleted: %s [%s]' % (name, checksum))
                        except PermissionError:
                            click.echo('[?] don\'t have permission to delete a duplicated file: %s' % path)
                else:
                    checksums.add(checksum)
                    if verbose >= 3:
                        click.echo('[+] file checksum added: %s [%s]' % (name, checksum))
            elif recursive and os.path.isdir(path):
                if verbose >= 2:
                    click.echo('[!] digging deeper into subdirectory: %s' % path)
                check_dir(path)
                # The reason why I am checking if the directory is empty here
                # is because maybe it was full of duplicated files and I am
                # the one who delete all the files inside.
                if not no_delete_empty and not check_only and len(os.listdir(path)) <= 0:
                    try:
                        os.rmdir(path)
                        if verbose >= 2:
                            click.echo('[-] removed empty subdirectory: %s' % path)
                    except PermissionError:
                        click.echo('[?] don\'t have permission to delete an empty subdirectory: %s' % path)

            time.sleep(sleep_time)

    for d in dirs:
        if verbose >= 2:
            click.echo('[!] checking directory: %s' % d)
        check_dir(d)

    click.echo('\n\n%d file(s) duplicated, sized %d byte(s)' % (duplicated, size))


if __name__ == '__main__':
    dupdel()
