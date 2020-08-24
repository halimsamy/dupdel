# dupdel
check duplicated file and delete them using hash checksums.

# Why I made this?
I was looking into my PC, Extrnal HDDs and Cloud, I found them a miss!, A lot of duplicated files everywhere and I have no time to check them by hand.
But wait! The PC can do this for me and.... TAAARAAA!
Opened my code editor, wrote 80 line of python code in couple of minutes, and here we go... XD
(NOTE: not very perfect but it works and this is what I want.)

# Usage
**Tested on Linux Only!**
```
Usage: dupdel.py [OPTIONS] DIRS...

  Check duplicated file and delete them using hash checksums.

Options:
  -c, --chunk-size INTEGER RANGE  The size of every chunk of the file to read
                                  and update the checksum. This value affects
                                  the Memory/CPU Usage as well as the progress
                                  speed.  [default: 4096]

  -s, --sleep-time FLOAT RANGE    The time to sleep (in seconds) while
                                  looping/iterating trow the files and calc
                                  the checksum. This was made to prevent CPU
                                  Leak (100% Usage on some platforms).
                                  [default: 0.001]

  -D, --no-delete-empty           Don't delete empty subdirectories.
  -S, --separate                  Delete duplicates in each directory
                                  separately.

  -C, --check-only                Check only, Don't delete anything.
  -R, --recursive                 Check files and directories recursively.
  -v, --verbose                   Output a diagnostic for every file
                                  processed.

  -h, --hash-type [md5|sha1|sha224|sha256|sha384|sha512]
                                  The hash type used to check the files'
                                  checksum.  [default: sha1]

  --help                          Show this message and exit.
```
