#!/usr/local/bin/python
"""
PyXm - metadata tags
Author : Edward Vetter-Drake
Version : 0.5
"""
import os
import eyed3

# TODO: disc_num, images, lyrics

def main():
    """pass"""
    pass

def bag_and_tag():
    """get metadata from filename and write to file"""
    filenames = get_mp3_names()
    for name in filenames:
        tags = dict({\
            'artist' : name.split('_-_')[2][:-4],\
            'album' : name.split('_-_')[1],\
            'title' : name.split('_-_')[0],\
        })
        set_id3_tags(name, **tags)


def get_mp3_names(folder='./'):
    """
    get all of the files in the current folder and return the names of the files.

    :returns: list of filenames
    :rtype: list
    """

    for _, __, files in os.walk(folder):
        mp3s = []
        for name in files:
            if 'mp3' in name:
                mp3s.append(name)
        return mp3s


def set_id3_tags(mp3filename, **kwargs):
    """load mp3 file, set tags and save"""

    audiofile = eyed3.load(mp3filename)
    set_tags(audiofile, **kwargs)
    write_tags_to_file(audiofile, mp3filename)


def set_tags(mp3data, **kwargs):
    """set tags to mp3"""

    mp3data.tag.artist = unicode(kwargs['artist'])
    mp3data.tag.album = unicode(kwargs['album'])
    mp3data.tag.title = unicode(kwargs['title'])


def get_tags(mp3data):
    """get tags from mp3"""

    mp3tags = { \
            'artist' : mp3data.tag.artist,\
            'album' : mp3data.tag.album,\
            'album_artist' : mp3data.tag.album_artist,\
            'title' : mp3data.tag.title,\
            'genre' : mp3data.tag.genre,\
            'play_count' : mp3data.tag.play_count\
            }
    return mp3tags

def write_tags_to_file(mp3data, filename):
    """save the file"""

    mp3data.tag.save(filename)


if __name__ == '__main__':
    main()
