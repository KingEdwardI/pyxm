## PyXm

Batch download music from youtube utilizing the spotify api

#### Version 3 : User Interface

* v3.0 : user interface

## Version 2 : Improved CLI + Spotify + Formatting
Improved CLI 

  * help menu
  * progress bar

Spotify API

  * No need for API key
  * searches are more reliable

Formatting

  * Downloaded files have formatted names
  * con create folders based on albums
  * can take id3 metadata from filenames


## Getting Started

### Prerequisites

* Python

### Installation

##### auto

`./install.sh`

##### manual

`pip install -r $HOME/.pyxm/requirements.txt`

`alias pyxm=$HOME/.pyxm/pyxm_2_0/pyxm/pyxm.py`


## Usage

##### Create a new directory for download and navigate into that directory to run the program

```
Usage:
    pyxm download (-a | -l | -t) [-v | -x | -i] QUERY
    pyxm search (-a | -l | -t) QUERY
    pyxm format [-y] [-m | -f | -c]
    pyxm [-h | --help]
    pyxm --version

Options:
    -h --help       Show this screen.
    -a              specify artist query
    -l              specify album query
    -t              specify track query
    -i              input a spotify id
    -x              run formatting immediately after download completes
    -v              display debugging details
    -m              get metadata from filenames and write to file
    -f              create folder structure and move files
    -y              yes, format everything
    -c              cleanup CWD by removing all non-mp3s
    --version       show program version

Commands:
    download        specify artist, album, or track, query
                    for respective item and download what is found

    search          specify artist, album, or track, query
                    for respective item and display what is found

    format          format metadata, folder structure, or cleanup cwd.

```

## Running Tests

## Contributing

For the time being just use the app and submit issues.


## Disclaimer

Downloading copyrighted material may be illegal in your country. Use at your own risk.

## Authors

* <b>Edward Vetter-Drake</b> - PyXm 

## Acknowledgements

* <a href="https://github.com/yask123">Yask123</a>

> Inspiration from Yask123 Instant-Music-Downloader

* <a href="https://rg3.github.io/youtube-dl/">Youtube-dl</a>

> Could not be done without YT-DL

## License

PyXm - Utilize the spotify API to download songs from youtube

Copyright (C) 2017 Edward Vetter-Drake

This file is part of PyXm

PyXm is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyXm is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
