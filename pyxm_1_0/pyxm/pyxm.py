#!/usr/local/bin/python
# PyXm - CLI
# Author : Edward Vetter-Drake
# Version : 2.0
import sys

import menu
import spotify.search as spit
import spotify.download as splat
import metadata.id3tags as tagme
import metadata.folders as crease
import metadata.cleanup as broomstick

def main():

    if menu.helpmenu['download']:
        if menu.helpmenu['-a']:
            print 'download artist ' + menu.helpmenu['QUERY']
            try:
                if menu.helpmenu['-v']:
                    splat.download_artist(spit.artist_search(menu.helpmenu['QUERY'])[0]['uri'], quiet=False)
                else:
                    splat.download_artist(spit.artist_search(menu.helpmenu['QUERY'])[0]['uri'])
            except IndexError:
                print 'No artists found matching that query'
        elif menu.helpmenu['-l']:
            print 'download album ' + menu.helpmenu['QUERY']
            try:
                if menu.helpmenu['-v']:
                    splat.download_album(spit.album_search(menu.helpmenu['QUERY'])[0]['uri'], quiet=False)
                else:
                    splat.download_album(spit.album_search(menu.helpmenu['QUERY'])[0]['uri'])
            except IndexError:
                print 'No albums found matching that query'
        elif menu.helpmenu['-t']:
            print 'download track ' + menu.helpmenu['QUERY']
            splat.download_track(spit.track_search(menu.helpmenu['QUERY'])[0])
        else:
            print 'please specify a download type'

    elif menu.helpmenu['search']:
        if menu.helpmenu['-a']:
            print 'search artist: ' + menu.helpmenu['QUERY']
            if len(spit.artist_search(menu.helpmenu['QUERY'])) == 0:
                print 'no artists found matching that query'
            else:
                print spit.artist_search(menu.helpmenu['QUERY'])
        elif menu.helpmenu['-l']:
            print 'search album: ' + menu.helpmenu['QUERY']
            if len(spit.album_search(menu.helpmenu['QUERY'])) == 0:
                print 'No albums found matching that query'
            else:
                print spit.album_search(menu.helpmenu['QUERY'])
        elif menu.helpmenu['-t']:
            print 'search track: ' + menu.helpmenu['QUERY']
            print spit.track_search(menu.helpmenu['QUERY'])
        else:
            print 'please specify a search type'

    elif menu.helpmenu['format']:
        if menu.helpmenu['-m']:
            print 'formatting id3 tags...'
            tagme.bagAndTag()
        elif menu.helpmenu['-f']:
            print 'creating folders and moving files...'
            crease.makeAndMove()
        elif menu.helpmenu['-c']:
            print 'cleaning directory...'
            broomstick.removeJunk() 
        else:
            format_ = raw_input('Are you sure you want to format everything? (y/N) >')
            if format_.lower() == 'y':
                print 'formatting id3 tags...'
                tagme.bagAndTag()
                print 'creating folders and moving files...'
                crease.makeAndMove()
                print 'cleaning directory...'
                broomstick.removeJunk() 
            else:
                print menu.PYXM
                print menu.helpmsg 


    else:
        print menu.PYXM
        print menu.helpmsg 
    

if __name__ == '__main__':
    main()
