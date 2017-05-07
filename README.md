## PyXm

Batch download music from youtube utilizing the spotify api

### Upcoming features

#### Version 2 :
* choose what to download from a search

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

`git clone https://github.com/KingEdwardI/pyxm $HOME/.pyxm`

`pip install -r $HOME/.pyxm/requirements.txt`

`alias pyxm=$HOME/.pyxm/pyxm_2_0/pyxm.py`

## Usage

##### Create a new directory for download and navigate into that directory to run the program

```
Usage:
    pyxm download (-a | -l | -t) [-v] QUERY
    pyxm search (-a | -l | -t) QUERY
    pyxm format [-y] [-m | -f | -c] 
    pyxm [-h | --help] 
    pyxm --version
    
Options:
    -h --help       Show this screen and exit
    -a              specify artist query
    -l              specify album query
    -t              specify track query
    -v              display debugging details
    -m              get metadata from filenames and write to file
    -f              create folder structure and move files
    -y              yes, format everything
    -c              cleanup CWD by removing all non-mp3s
    --version       show program version

Commands:
    download        specify artist, album, or track, query for respective item and download what is found
    search          specify artist, album, or track, query for respective item and display what is found
    format          format metadata, folder structure, or cleanup cwd.
    
```

## Running Tests


## Authors
* <b>Edward Vetter-Drake</b> - PyXm 

## Acknowledgements
* <a href="https://github.com/yask123">Yask123</a>

> Inspiration from Yask123 Instant-Music-Downloader

* <a href="https://rg3.github.io/youtube-dl/">Youtube-dl</a>

> Could not be done without YT-DL
