#!/usr/local/bin/python
import os

def main():
    pass

def findJunk(folder='./'):
    junk = []
    for _, __, files in os.walk(folder):
        for fn in files:
            if 'mp3' not in fn:
                junk.append(fn)
    return junk

def removeJunk(folder='./'):
    junk = findJunk(folder)
    for i in junk:
        os.remove(i)
        print 'removed file: ' + i 


if __name__ == '__main__':
    main()

