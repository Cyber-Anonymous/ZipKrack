<h1 align="center">ZipKrack v1.2.0</h1>
<p align="center"><img src="images/ZipKrack.png" alt="ZipKrack Logo">
</p>

# ZipKrack
ZipKrack is a tool designed to crack the passwords of ZIP files. It offers a simple and effective way to recover passwords used to secure zip archives.

# Tested on
- Kali Linux
- Ubuntu
- Termux

# Installation
`apt install python3`

`apt install git`

`git clone https://github.com/Cyber-Anonymous/ZipKrack.git`

`cd ZipKrack`

`python3 zipkrack.py`

# Usage
```bash

usage: zipkrack.py [-h] [-z ZIPFILE] [-w WORDLIST] [-o OUTPUT] [--version]

A tool for cracking passwords of encrypted ZIP files using a provided wordlist.

options:
  -h, --help            show this help message and exit
  -z ZIPFILE, --zipfile ZIPFILE
                        Specify the ZIP file.
  -w WORDLIST, --wordlist WORDLIST
                        Specify the password list.
  -o OUTPUT, --output OUTPUT
                        Directory to extract the contents of the ZIP file if the password is found
                        (default: Extract).
  --version             show program's version number and exit
                                                                                                         
```

## Screenshot

<p align="center">
    <img src="images/image.png" alt="ZipKrack Screenshot">
</p>

# Warning
**This tool is intended for educational purposes only. The developers are not responsible for any misuse or illegal activities conducted with this tool.**
