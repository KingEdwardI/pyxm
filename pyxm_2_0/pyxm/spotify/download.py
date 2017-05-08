#!/usr/local/bin/python
"""
PyXm - CLI
Author : Edward Vetter-Drake
Version : 1.5
"""
import sys
import itertools

from tqdm import tqdm

import ixm
import search

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    """pass"""
    pass

def download_artist(artist_id, quiet=True):
    """artist_id passed in as a string."""

    album_res = search.get_artist_albums(artist_id)['items']
    tracks = []
    for album in album_res:
        tracks.append(search.get_album_tracks(album['uri'])['items'])
    flat_tracks = list(itertools.chain(*tracks))
    for track in tqdm(flat_tracks, desc='Downloading...', unit='track'):
        try:
            track_details = search.get_track(track['uri'])
            pyxm_track = search.make_track(track_details)
            download_track(pyxm_track, quiet)
        except Exception as err:
            if not quiet:
                print err

def download_album(album_id, quiet=True):
    """album_id is passed in as a string."""

    tracks = search.get_album_tracks(album_id)['items']
    for track in tqdm(tracks, desc='Downloading...', unit='track'):
        try:
            download_track(search.make_track(search.get_track(track['uri'])), quiet)
        except Exception as err:
            if not quiet:
                print err


def download_track(track, quiet=True):
    """
    track is passed in as a dict and downloaded with ixm module.

    sampleTrack = {\
        'track': u'Hello',\
        'album': u'Hello',\
        'uri': u'spotify:track:0ENSn4fwAbCGeFGVUbXEU3',\
        'artist': u'Adele'\
    }
    """

    filename = quote_argument(track['track'] + '_-_' + track['album'] + '_-_' + track['artist'])

    track_queri = track['track'] + ' - ' + track['artist']
    track_query = track_queri.replace(u'\xd6', 'O').replace(u'\xf4', 'o').decode('ascii', 'ignore')

    # returns the first result of the track query to youtube
    video = ixm.search_videos(track_query)[0]
    if not quiet:
        print '[ORIGINAL QUERY]', track_query
        print '[YOUTUBE TITLE]: ', video[0]
        print '[YOUTUBE URL]: ', video[1]
    ixm.download_direct(video, filename, quiet) # download the video


def quote_argument(argument):
    """format a string to pass to the shell"""
    return '%s' % (
        argument
        .replace('/', '.')
        .replace('\\', '\\\\')
        .replace('"', '\\"')
        .replace('$', '\\$')
        .replace('`', '\\`')
    )

if __name__ == '__main__':
    main()
