#!/usr/local/bin/python
"""
PyXm - Search functions
Author : Edward Vetter-Drake
Version : 1.5
"""

import spotipy
SP = spotipy.Spotify()

def main():
    """pass"""
    pass


def artist_search(artist_query, limit_=10):
    """
    search spotify for a list of artists

    :returns: a list of artist details
    :rtype: list
    """
    results = SP.search(artist_query, type='artist', limit=limit_)
    artists = results['artists']['items']
    artistlist = []
    for artist in artists:
        artistlist.append({ \
            'artist': artist['name'], \
            'image': type(artist['images']), \
            'uri': artist['uri'] \
            })

    return artistlist


def album_search(album_query, limit_=10):
    """
    search spotify for a list of albums

    :returns: a list of album details
    :rtype: list
    """
    results = SP.search(album_query, type='album', limit=limit_)
    albums = results['albums']['items']

    return make_albums(albums)


def make_albums(albums):
    if type(albums) == dict:
        albums = albums['items']

    albumlist = []
    for album in albums:
        albumlist.append({
            'album': album['name'], \
            'artist': album['artists'][0]['name'], \
            'uri': album['uri'] \
            })
    return albumlist


def track_search(track_query, limit_=10):
    """
    search spotify for a list of tracks

    :returns: a list of track details
    :rtype: list
    """
    results = SP.search(track_query, type='track', limit=limit_)
    tracks = results['tracks']['items']
    tracklist = []
    for track in tracks:
        tracklist.append(make_track(track))

    return tracklist

def make_track(track, album=None):
    """
    build relevant track details

    :rtype: dict{}
    :keys: track, album, artist, uri
    """
    return({ \
        'track': track['name'], \
        'album': album or track['album']['name'], \
        'artist': track['album']['artists'][0]['name'], \
        'uri': track['uri'] \
    })

def get_artist_albums(artist_id, limit_=20):
    """make use of SP elsewhere"""
    return SP.artist_albums(artist_id, limit=limit_)

def get_album_tracks(album_id, limit_=50):
    """
    :returns: tracks of the album
    :rtype:
    """
    return SP.album_tracks(album_id, limit=limit_)

def get_track(trackId):
    return SP.track(trackId)

#  def playlist_search(playlist):
    #  pass


if __name__ == '__main__':
    main()
