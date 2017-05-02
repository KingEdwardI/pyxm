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

def main():

    if menu.helpmenu['download']:
        if menu.helpmenu['-a']:
            print 'download artist ' + menu.helpmenu['QUERY']
            splat.download_artist(spit.artist_search(menu.helpmenu['QUERY'])[0]['uri'])
        elif menu.helpmenu['-l']:
            print 'download album ' + menu.helpmenu['QUERY']
            splat.download_album(spit.album_search(menu.helpmenu['QUERY'])[0]['uri'])
        elif menu.helpmenu['-t']:
            print 'download track ' + menu.helpmenu['QUERY']
            splat.download_track(spit.track_search(menu.helpmenu['QUERY'])[0])
        else:
            print 'please specify a download type'

    elif menu.helpmenu['search']:
        if menu.helpmenu['-a']:
            print 'search artist: ' + menu.helpmenu['QUERY']
            print spit.artist_search(menu.helpmenu['QUERY'])
        elif menu.helpmenu['-l']:
            print 'search album: ' + menu.helpmenu['QUERY']
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
        else:
            print menu.PYXM
            print menu.helpmsg 

    else:
        print menu.PYXM
        print menu.helpmsg 
    

if __name__ == '__main__':
    main()
