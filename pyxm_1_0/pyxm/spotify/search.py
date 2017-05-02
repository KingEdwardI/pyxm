#!/usr/bin/python

import spotipy, pprint, json
sp = spotipy.Spotify()
pp = pprint.PrettyPrinter(indent=1)

def main():
    pass


def makeFileName(trackId):
    """
    create a filename based on the information from the ID of a track from Spotify

    :returns: formatted output filename
    :rtype: str
    """
    track = sp.track(trackId)
    album = track['album']['name']
    artist = track['artists'][0]['name']
    return artist + ' - ' + album + ' - ' + track['name']


def artist_search(artist, limit_ = 10):
    """
    search spotify for a list of artists

    :returns: a list of artist details
    :rtype: list
    """
    results = sp.search(artist, type='artist', limit=limit_)
    artists = results['artists']['items']
    artistlist = []
    for artist in artists:
        artistlist.append({ \
            'artist': artist['name'], \
            'image': type(artist['images']), \
            'uri': artist['uri'] \
            })

    return artistlist


def album_search(album, limit_ = 10):
    """
    search spotify for a list of albums

    :returns: a list of album details
    :rtype: list
    """
    results = sp.search(album, type='album', limit=limit_)
    albums = results['albums']['items']
    albumlist = []
    for album in albums:
        albumlist.append({
            'album': album['name'], \
            'artist': album['artists'][0]['name'], \
            'uri': album['uri'] \
            })

    return albumlist


def track_search(track, limit_ = 10):
    """
    search spotify for a list of tracks

    :returns: a list of track details
    :rtype: list
    """
    results = sp.search(track, type='track', limit=limit_)
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

def get_artist_albums(artistId, limit_=20):
    return sp.artist_albums(artistId, limit=limit_)

def get_album_tracks(albumId, limit_=50):
    """
    :returns: tracks of the album
    :rtype:
    """
    album_tracks = sp.album_tracks(albumId, limit=limit_)
    return album_tracks

def get_track(trackId):
    return sp.track(trackId)

def playlist_search(playlist):
    pass


if __name__ == '__main__':
    main()
