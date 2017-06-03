#!/usr/local/bin/python
"""
PyXm - CLI
Author : Edward Vetter-Drake
Version : 2.0
"""
import pprint

import menu
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

    print "download not currently functional"
    pass

def artist_download():
    """artist download"""
    pass


def album_download():
    """album download"""
    pass


def track_download():
    """track download"""
    pass


def search_menu():
    """search menu"""

    print "search not currently functional"
    pass

def artist_search():
    """artist search"""
    pass


def album_search():
    """album search"""
    pass


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
