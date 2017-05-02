#!/usr/local/bin/python
import os, eyed3

"""
album
album_artist
album_type
artist
disc_num
genre
images
lyrics
title
play_count
"""

def main():
    pass

def bagAndTag():
    filenames = getMp3Names()
    for name in filenames:
        tags = dict({\
            'artist' : name.split('_-_')[2][:-4],\
            'album' : name.split('_-_')[1],\
            'title' : name.split('_-_')[0],\
        })
        setId3Tags(name, **tags)


def getMp3Names(folder='./'):
    """
    get all of the files in the current folder and return the names of the files.

    :returns: list of filenames
    :rtype: list
    """

    for _, __, files in os.walk(folder):
        mp3s = []
        for fn in files:
            if 'mp3' in fn:
                mp3s.append(fn)
        return mp3s


def setId3Tags(mp3filename, **kwargs):

    audiofile = loadMp3(mp3filename)
    setTags(audiofile, **kwargs)
    writeTagsToFile(audiofile, mp3filename)


def loadMp3(filename):

    return eyed3.load(filename)


def setTags(mp3data, **kwargs):

    mp3data.tag.artist = unicode(kwargs['artist'])
    mp3data.tag.album = unicode(kwargs['album'])
    mp3data.tag.title = unicode(kwargs['title'])


def getTags(mp3data):

    mp3tags = { \
            'artist' : mp3data.tag.artist,\
            'album' : mp3data.tag.album,\
            'album_artist' : mp3data.tag.album_artist,\
            'title' : mp3data.tag.title,\
            'genre' : mp3data.tag.genre,\
            'play_count' : mp3data.tag.play_count\
            }
    return mp3tags

def writeTagsToFile(mp3data, filename):

    mp3data.tag.save(filename)


if __name__ == '__main__':
    main()
