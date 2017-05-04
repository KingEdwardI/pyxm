#!/usr/local/bin/python
from docopt import docopt

helpmsg = """
Usage:
    pyxm download (-a | -l | -t) QUERY
    pyxm search (-a | -l | -t) QUERY
    pyxm format [-m | -f | -c]
    pyxm [-h | --help] 
    pyxm --version
    
Options:
    -h --help       Show this screen.
    -a              specify artist query
    -l              specify album query
    -t              specify track query
    -m              get metadata from filenames and write to file
    -f              create folder structure and move files
    -c              cleanup CWD by removing all non-mp3s
    --version       show program version
    
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
