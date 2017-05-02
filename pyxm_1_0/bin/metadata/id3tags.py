#!/usr/local/bin/python
import eyed3
import os
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
    filenames = getFileNames()
    for name in filenames:
        if name[-4:] == '.mp3':
            tags = dict({\
                'artist' : name.split('_-_')[2][:-4],\
                'album' : name.split('_-_')[1],\
                'title' : name.split('_-_')[0],\
            })
            setId3Tags(name, **tags)


def getFileNames():
    """
    get all of the files in the current folder and return the names of the files.

    :returns: list of filenames
    :rtype: list
    """

    for _, __, files in os.walk('./'):
        return files


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
