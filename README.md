# dupdel
dupdel is a Python tool that checks for duplicated files and provides the option to delete them using hash checksums. It helps you declutter your storage by identifying and removing duplicate files efficiently.

## Motivation
As a software developer and computer science student, I often found my devices filled with duplicated files scattered across my PC, external HDDs, and cloud storage. Manually checking and cleaning them was time-consuming and tedious. That's when I decided to create dupdel. In just a few minutes, I wrote an 80-line Python script to automate this process, making it much easier to manage my files.

While dupdel may not be perfect, it gets the job done, helping you reclaim valuable storage space.

## Requirements
[Click](https://click.palletsprojects.com/en/7.x/)
```
pip install -U click
```

## Usage
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

## Contributing
Contributions are welcome! If you have any ideas for improving dupdel or encounter issues, please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
