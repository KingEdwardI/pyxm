#!/usr/bin/python
# PyXm - CLI
# Author : Edward Vetter-Drake
# Version : 1.5
import sys
import helpmenu
import spotify.search as spit
import spotify.download as splat

def main():

    if helpmenu.helpmenu['download']:
        if helpmenu.helpmenu['-a']:
            print 'download artist ' + helpmenu.helpmenu['QUERY']
            splat.download_artist(spit.artist_search(helpmenu.helpmenu['QUERY'])[0]['uri'])
        elif helpmenu.helpmenu['-l']:
            print 'download album ' + helpmenu.helpmenu['QUERY']
            splat.download_album(spit.album_search(helpmenu.helpmenu['QUERY'])[0]['uri'])
        elif helpmenu.helpmenu['-t']:
            print 'download track ' + helpmenu.helpmenu['QUERY']
            splat.download_track(spit.track_search(helpmenu.helpmenu['QUERY'])[0])
        else:
            print 'please specify a download type'

    elif helpmenu.helpmenu['search']:
        if helpmenu.helpmenu['-a']:
            print 'search artist: ' + helpmenu.helpmenu['QUERY']
            print spit.artist_search(helpmenu.helpmenu['QUERY'])
        elif helpmenu.helpmenu['-l']:
            print 'search album: ' + helpmenu.helpmenu['QUERY']
            print spit.album_search(helpmenu.helpmenu['QUERY'])
        elif helpmenu.helpmenu['-t']:
            print 'search track: ' + helpmenu.helpmenu['QUERY']
            print spit.track_search(helpmenu.helpmenu['QUERY'])
        else:
            print 'please specify a search type'

    else:
        print helpmenu.PYXM
        print helpmenu.helpmsg 
    

if __name__ == '__main__':
    main()
