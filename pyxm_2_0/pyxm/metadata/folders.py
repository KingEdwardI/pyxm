#!/usr/local/bin/python
import os

import id3tags as tagme

def main():
    pass

def makeAndMove():
    makeAlbumFolders()
    moveFiles()

def moveFiles():
    mp3s = tagme.getMp3Names()
    for mp3 in mp3s:
        os.rename(os.path.abspath(mp3), os.path.dirname(os.path.abspath(mp3)) + '/' + mp3.split('_-_')[1] + '/' + mp3)

def makeAlbumFolders():
    # TODO: find album date from spotipy and include in folder name

    mp3s = tagme.getMp3Names()
    for mp3 in mp3s:
        try:
            os.mkdir(mp3.split('_-_')[1])
        except OSError:
            pass


if __name__ == '__main__':
    main()
    
