#!/usr/local/bin/python
from docopt import docopt

helpmsg = """
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
    
"""

helpmenu = docopt(helpmsg, version='PyXm 1.2')

PYXM = """
::::::::   :::        ::: :::       ::: ::::::       ::::::        @@@@@@@@@@@@@@
:::   :::   :::      :::   :::     :::  ::: :::     ::: :::        @@@@@@@@@@@@@@
::      ::   :::    :::     :::   :::   :::  :::   :::  :::        @@          @@
:::   :::     :::  :::       ::: :::    :::   ::: :::   :::        @@          @@
:::::::        ::::::         :::::     :::    :::::    :::   .....@@     .... @@
:::             ::::         ::: :::    :::             :::  @@@@@@@@    @@@@@@@@
:::             ::::        :::   :::   :::             ::: @@@@@@@@@   @@@@@@@@@
:::             ::::       :::     :::  :::             :::  @@@@@@@     @@@@@@@
:::             ::::      :::       ::: :::             :::   @@@@        @@@@   
"""
