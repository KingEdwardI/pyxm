#!/usr/local/bin/python
"""
PyXm - CLI
Author : Edward Vetter-Drake
Version : 2.0
"""
import pprint

import menu
import spotify.search as spit
import spotify.download as splat
import metadata.id3tags as tagme
import metadata.folders as crease
import metadata.cleanup as broomstick

PP = pprint.PrettyPrinter(indent=2)

def main():
    """Run program"""

    # Download
    if menu.helpmenu['download']:
        download_menu()

    # Search
    elif menu.helpmenu['search']:
        search_menu()

    # Formatting
    elif menu.helpmenu['format']:
        format_menu()

    else:
        print menu.PYXM
        print menu.helpmsg

def download_menu():
    """download menu"""

    # Artist flag
    if menu.helpmenu['-a']:
        print 'download artist ' + menu.helpmenu['QUERY']
        artist_download()
    # Album flag
    elif menu.helpmenu['-l']:
        print 'download album ' + menu.helpmenu['QUERY']
        album_download()
    # Track flag
    elif menu.helpmenu['-t']:
        print 'download track ' + menu.helpmenu['QUERY']
        track_download()
    else:
        print 'please specify a download type'


def artist_download():
    """artist download"""

    try:
        query = menu.helpmenu['QUERY']

        # Verbose
        if menu.helpmenu['-v']:
            splat.download_artist(spit.artist_search(query)[0]['uri'], quiet=False)

        # Format
        elif menu.helpmenu['-x']:
            splat.download_artist(spit.artist_search(query)[0]['uri'])
            format_folder()

        # Input Spotify URI
        elif menu.helpmenu['-i']:
            splat.download_artist(query)
            if menu.helpmenu['-x']:
                format_folder()

        # Default
        else:
            splat.download_artist(spit.artist_search(query)[0]['uri'])

    except IndexError:
        print 'No artists found matching that query'


def album_download():
    """album download"""

    try:
        query = menu.helpmenu['QUERY']

        # Verbose
        if menu.helpmenu['-v']:
            splat.download_album(spit.album_search(query)[0]['uri'], quiet=False)

        # Format
        elif menu.helpmenu['-x']:
            splat.download_album(spit.album_search(query)[0]['uri'])
            format_folder()

        # Input Spotify URI
        elif menu.helpmenu['-i']:
            splat.download_album(spit.album_search(query))
            if menu.helpmenu['-x']:
                format_folder()

        # Default
        else:
            splat.download_album(spit.album_search(query)[0]['uri'])

    except IndexError:
        print 'No albums found matching that query'


def track_download():
    """track download"""

    # Verbose
    if menu.helpmenu['-v']:
        splat.download_track(spit.track_search(menu.helpmenu['QUERY'])[0], quiet=False)

    # Format
    elif menu.helpmenu['-x']:
        print 'formatting not available for single track'

    # Input Spotify URI
    elif menu.helpmenu['-i']:
        splat.download_track(spit.track_search(menu.helpmenu['QUERY']))


def search_menu():
    """search menu"""

    # Artist
    if menu.helpmenu['-a']:
        artist_search()
    # Album
    elif menu.helpmenu['-l']:
        album_search()
    # Track
    elif menu.helpmenu['-t']:
        print 'search track: ' + menu.helpmenu['QUERY']
        print PP.pprint(spit.track_search(menu.helpmenu['QUERY']))
    else:
        print 'please specify a search type'

def artist_search():
    """artist search"""

    print 'search artist: ' + menu.helpmenu['QUERY']
    if not spit.artist_search(menu.helpmenu['QUERY']):
        print 'no artists found matching that query'
    else:
        PP.pprint(spit.artist_search(menu.helpmenu['QUERY']))


def album_search():
    """album search"""

    print 'search album: ' + menu.helpmenu['QUERY']
    if 'spotify:artist:' in menu.helpmenu['QUERY']:
        albumlist = spit.get_artist_albums(menu.helpmenu['QUERY'])
        print albumlist
        PP.pprint(spit.make_albums(albumlist))
    elif not spit.album_search(menu.helpmenu['QUERY']):
        print 'No albums found matching that query'
    else:
        PP.pprint(spit.album_search(menu.helpmenu['QUERY']))


def format_menu():
    """format menu"""

    # Id3 tags
    if menu.helpmenu['-m']:
        print 'formatting id3 tags...'
        tagme.bag_and_tag()

    # Folders
    elif menu.helpmenu['-f']:
        print 'creating folders and moving files...'
        crease.make_and_move()

    # Clean
    elif menu.helpmenu['-c']:
        print 'cleaning directory...'
        broomstick.remove_junk()

    # All
    else:
        if menu.helpmenu['-y']:
            format_folder()
        else:
            format_ = raw_input('Are you sure you want to format everything? (y/N) >')
            if format_.lower() == 'y':
                format_folder()



def format_folder():
    """format the current working directory"""

    print 'formatting id3 tags...'
    tagme.bag_and_tag()
    print 'creating folders and moving files...'
    crease.make_and_move()
    print 'cleaning directory...'
    broomstick.remove_junk()



if __name__ == '__main__':
    main()
