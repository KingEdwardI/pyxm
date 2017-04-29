#!/usr/bin/python
# PyXm - CLI
# Author : Edward Vetter-Drake
# Version : 1.5
from urllib import quote_plus as qp
import os, sys, urllib
import ixm2
import search

# PYXM = """""" # TODO
# helpmenu = """""" # TODO
# welcome = """""" # TODO
sampleTrack = {'track': u'Hello', 'album': u'Hello', 'uri': u'spotify:track:0ENSn4fwAbCGeFGVUbXEU3', 'artist': u'Adele'}
sampleArtist = {'uri': u'spotify:artist:7mnBLXK823vNxN3UWB7Gfz', 'artist': u'The Black Keys'}


def main():
    pass

def download_artist(artistId):
    album_res = search.get_artist_albums(artistId)['items']
    albumDict = {}
    print album_res
    for album in album_res:
        albumDict[album['name']] = []
        download_album(album['uri'])
        
def download_album(albumId):
    tracks = search.get_album_tracks(albumId)['items']
    for track in tracks:
        try:
            download_track(search.make_track(search.get_track(track['uri'])))
        except:
            pass

def download_track(track):
    filename = track['track'] + ' - ' + track['album'] + ' - ' + track['artist']
    track_query = track['track'] + ' - ' + track['artist']

    video = ixm2.search_videos(track_query)[0]
    ixm2.download_direct(video, filename)


    

if __name__ == '__main__':
    main()
