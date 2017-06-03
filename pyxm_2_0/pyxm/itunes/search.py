import itunes

artist = 'Eminem'
iArtist = itunes.search_artist(artist)[0]
iAlbums = iArtist.get_albums()
iTracks = []

for album in iAlbums:
    obj = {}
    obj['album'] = album
    obj['tracks'] = album.get_tracks()
    iTracks.append(obj)

for album in iTracks:
    for track in album['tracks']:
        print str(track) + ' - ' + artist

#  print iArtist, iAlbums
