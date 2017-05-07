#!/usr/local/bin/python
"""
PyXm - Cleanup
Author : Edward Vetter-Drake
Version : 0.5
"""
import os

def main():
    """pass"""
    pass

def find_junk(folder='./'):
    """find anything that is not an mp3"""
    junk = []
    bad_types = ['.part', '.webm']
    for _, __, files in os.walk(folder):
        for name in files:
            if any(word in name for word in bad_types):
                junk.append(name)
    return junk


def remove_junk(folder='./'):
    """remove anything that was found"""
    junk = find_junk(folder)
    for i in junk:
        os.remove(i)
        print 'removed file: ' + i


if __name__ == '__main__':
    main()
