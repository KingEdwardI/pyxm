#!/usr/bin/python
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

    if menu.menu['download']:
        if menu.menu['-a']:
            print 'download artist ' + menu.menu['QUERY']
            splat.download_artist(spit.artist_search(menu.menu['QUERY'])[0]['uri'])
        elif menu.menu['-l']:
            print 'download album ' + menu.menu['QUERY']
            splat.download_album(spit.album_search(menu.menu['QUERY'])[0]['uri'])
        elif menu.menu['-t']:
            print 'download track ' + menu.menu['QUERY']
            splat.download_track(spit.track_search(menu.menu['QUERY'])[0])
        else:
            print 'please specify a download type'

    elif menu.menu['search']:
        if menu.menu['-a']:
            print 'search artist: ' + menu.menu['QUERY']
            print spit.artist_search(menu.menu['QUERY'])
        elif menu.menu['-l']:
            print 'search album: ' + menu.menu['QUERY']
            print spit.album_search(menu.menu['QUERY'])
        elif menu.menu['-t']:
            print 'search track: ' + menu.menu['QUERY']
            print spit.track_search(menu.menu['QUERY'])
        else:
            print 'please specify a search type'

    elif menu.menu['format']:
        if menu.menu['-m']:
            print 'formatting id3 tags...'
            tagme.bagAndTag()
        elif menu.menu['-f']:
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
