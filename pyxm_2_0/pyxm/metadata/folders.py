#!/usr/local/bin/python
"""
PyXm - Folders
Author : Edward Vetter-Drake
Version : 0.5
"""
import os

import id3tags as tagme

def main():
    """pass"""
    pass

def make_and_move():
    """run functions"""
    make_album_folders()
    move_files()

def move_files():
    """move files into structured folders"""
    mp3s = tagme.getMp3Names()
    for mp3 in mp3s:
        old_file = os.path.abspath(mp3)
        new_file = os.path.dirname(os.path.abspath(mp3))
        os.rename(old_file,\
            new_file + \
            '/' + mp3.split('_-_')[1] + \
            '/' + mp3 \
        )

def make_album_folders():
    """create folders from filenames"""
    # TODO: find album date from spotipy and include in folder name

    mp3s = tagme.getMp3Names()
    for mp3 in mp3s:
        try:
            os.mkdir(mp3.split('_-_')[1])
        except OSError:
            pass


if __name__ == '__main__':
    main()
