## PyXm

Easily install music utilizing last.fm and youtube-dl

### Upcoming features

* v1.1 : search functions
* v1.2 : create directories
* v1.3 : pandora tracklist search
* v1.4 : soundcloud tracklist search
* v1.5 : spotify tracklist search

* v2.0 : user interface

## Getting Started

You will need an api-key from <a href="last.fm/api">last.fm</a>

### Prerequisites
* Python
* <a href="https://rg3.github.io/youtube-dl/download.html">youtube-dl</a>


### Installation

`python super_installer.py`

you will be prompted for an API key, without a valid last.fm API key, this will not work.

## Usage
From anywhere in the command line (preferably a new folder) run `pyxm`. Currently pyxm will download into the current working directory.

#### CLI Commands:

```
    help, h: display this message and return to pyxm console
    
    turbo, X, zoom: will toggle turbo mode !!! This WILL cause serious system resource usage, use with caution !!!
    
    quiet, q, shh: will toggle quiet mode
    
    artist, a: enter an artist search line where you will be
        prompted for an artist and it will download all
        tracks found for that artist
        
    album, l: enter an album search line where you will be
        prompted for an album and it will download all
        tracks found for that album
        
    track, t: enter a song search line where you will be
        prompted for a song, which will create a list and
        download when you exit the line
        
    exit: will quit PyXm
```

## Running Tests

Tests run with Pytest

## Authors
* <b>Edward Vetter-Drake</b> - PyXm 

## Acknowledgements
* <a href="https://github.com/yask123">Yask123</a>

> Inspiration from Yask123 Instant-Music-Downloader

* <a href="https://rg3.github.io/youtube-dl/">Youtube-dl</a>

> Could not be done without YT-DL