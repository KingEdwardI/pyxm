#!/usr/local/bin/python
# PyXm - CLI
# Author : Edward Vetter-Drake
# Version : 1.5
from urllib import quote_plus as qp
import os, sys, urllib
import ixm
import search

def main():
    pass

def download_artist(artistId):
    """artistId passed in as a string."""
    album_res = search.get_artist_albums(artistId)['items']
    albumDict = {}
    for album in album_res:
        albumDict[album['name']] = []
        download_album(album['uri'])
        
def download_album(albumId):
    """albumId is passed in as a string."""

    tracks = search.get_album_tracks(albumId)['items']
    for track in tracks:
        try:
            download_track(search.make_track(search.get_track(track['uri'])))
        except Exception as e:
            print e

def download_track(track):
    """
    track is passed in as a dict and downloaded with ixm module.

    sampleTrack = {\
        'track': u'Hello',\
        'album': u'Hello',\
        'uri': u'spotify:track:0ENSn4fwAbCGeFGVUbXEU3',\
        'artist': u'Adele'\
    }
    """

    filename = track['track'] + '_-_' + track['album'] + '_-_' + track['artist']
    track_query = track['track'] + ' - ' + track['artist']

    video = ixm.search_videos(track_query)[0] # returns the first result of the track query to youtube
    print '[YOUTUBE TITLE]: ', video[0]
    print '[YOUTUBE URL]: ', video[1]
    ixm.download_direct(video, filename) # download the video

    

if __name__ == '__main__':
    main()
