#!/usr/local/bin/python
# PyXm - CLI
# Author : Edward Vetter-Drake
# Version : 1.5
from urllib import quote_plus as qp
import os, sys, urllib, itertools
import ixm
import search
from tqdm import tqdm

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    pass

def download_artist(artistId, quiet=True):
    """artistId passed in as a string."""

    album_res = search.get_artist_albums(artistId)['items']
    tracks = []
    for album in album_res:
        tracks.append(search.get_album_tracks(album['uri'])['items'])
    flatTracks = list(itertools.chain(*tracks))
    for track in tqdm(flatTracks, desc='Downloading...', unit='track'):
        try:
            download_track(search.make_track(search.get_track(track['uri'])), quiet)
        except Exception as e:
            if not quiet:
                print e
        
def download_album(albumId, quiet=True):
    """albumId is passed in as a string."""

    tracks = search.get_album_tracks(albumId)['items']
    for track in tqdm(tracks, desc='Downloading...', unit='track'):
        try:
            download_track(search.make_track(search.get_track(track['uri'])), quiet)
        except Exception as e:
            if not quiet:
                print e


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

    video = ixm.search_videos(track_query)[0] # returns the first result of the track query to youtube
    if not quiet:
        print '[ORIGINAL QUERY]', track_query
        print '[YOUTUBE TITLE]: ', video[0]
        print '[YOUTUBE URL]: ', video[1]
    ixm.download_direct(video, filename, quiet) # download the video

    
def quote_argument(argument):
    return '%s' % (
        argument
        .replace('/', '\\/')
        .replace('\\', '\\\\')
        .replace('"', '\\"')
        .replace('$', '\\$')
        .replace('`', '\\`')
    )

if __name__ == '__main__':
    main()
