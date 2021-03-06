#!/usr/local/bin/python
# PyXm - Download
# Author : Edward Vetter-Drake
# Version : 1.0
from bs4 import BeautifulSoup
import os
import requests
import re
import sys
import unicodedata as unicorn
import urllib
import urllib2
import json
from urllib import quote_plus as qp
from ._api_key import __api_key__

API_KEY=__api_key__
BASE_URL='http://ws.audioscrobbler.com'

#  songs = filter(None, (song.rstrip() for song in songs))
#  # strip out any new lines
#  songs = [qp(song.strip()) for song in songs if song]
#  song_list.extend(songs)


#  downloads = []
#  for song in song_list:
    #  downloads.append(query_and_download(song, prompt, quiet))
#  print('Downloaded: %s' % ', '.join(downloads))

def main():
    """ Run the program session """
    PYXM = """
∷∷∷∷∷∷∷∷   ∷∷∷        ∷∷∷ ∷∷∷       ∷∷∷ ∷∷∷∷∷∷       ∷∷∷∷∷∷        ∷∷∷∷∷∷∷∷∷∷∷∷∷∷
∷∷∷· ·∷∷∷   ∷∷∷      ∷∷∷   ∷∷∷     ∷∷∷  ∷∷∷ ∷∷∷     ∷∷∷ ∷∷∷        ∷∷∷∷∷∷∷∷∷∷∷∷∷∷
∷∷·    ·∷∷   ∷∷∷    ∷∷∷     ∷∷∷   ∷∷∷   ∷∷∷  ∷∷∷   ∷∷∷  ∷∷∷        ∷∷          ∷∷
∷∷∷· ·∷∷∷     ∷∷∷··∷∷∷       ∷∷∷ ∷∷∷    ∷∷∷   ∷∷∷·∷∷∷   ∷∷∷        ∷∷          ∷∷
∷∷∷∷∷∷∷        ∷∷∷∷∷∷         ∷∷·∷∷     ∷∷∷    ∷∷∷∷∷    ∷∷∷   ‥‥‥‥ ∷∷     ‥‥‥‥ ∷∷
∷∷∷             ∷∷∷∷         ∷∷∷ ∷∷∷    ∷∷∷             ∷∷∷  ∷∷∷∷∷∷∷∷    ∷∷∷∷∷∷∷∷
∷∷∷             ∷∷∷∷        ∷∷∷   ∷∷∷   ∷∷∷             ∷∷∷ ∷∷∷∷∷∷:∷∷   ∷∷∷∷∷∷∷∷∷
∷∷∷             ∷∷∷∷       ∷∷∷     ∷∷∷  ∷∷∷             ∷∷∷  ∷∷∷∷∷∷:     ∷∷∷∷∷∷:
∷∷∷             ∷∷∷∷      ∷∷∷       ∷∷∷ ∷∷∷             ∷∷∷   ∷∷∷∷        ∷∷∷∷   
"""
    helpMenu = """ 
Welcome to PyXm
::::::::::::::: \n
Commands: \n
    help, h: display this message and return to pyxm console
    turbo, T, zoom: will toggle turbo mode !!! This WILL cause serious system resource usage, use with caution !!!
    quiet, q, shh: will toggle quiet mode
    artist, a: enter an artist search line where you will be 
        prompted for an artist and it will download all 
        tracks found for that artist
    album, l: enter an album search line where you will be
        prompted for an album and it will download all 
        tracks found for that album
    track, s: enter a song search line where you will be 
        prompted for a song, which will create a list and 
        download when you exit the line 
    exit: will quit PyXm
"""

    print PYXM

    argument_string = ' '.join(sys.argv[1:])

    def main_cli(quiet, turbo):
        command = ''
        while command == '':
            command = raw_input('Enter command: ')

        cmd_case = qp(command)
        if cmd_case.lower() in ['help', 'h']:
            print helpMenu
            main_cli(quiet, turbo)

        elif cmd_case.lower() in ['artist', 'a']:
            if turbo:
                print 'Turbo is not allowed for artist search, turning off' # Seriously this will fuck shit up don't do it. 
                turbo = False

            try:
                artist = raw_input('Search for an artist (^C to quit, ^B to return to menu): ')
                
                if artist in ['^B', '']:
                    main_cli(quiet, turbo)

                trackList = tracks_from_artist(artist)
                if not len(trackList):
                    print "No Tracks Found"
                    main_cli(quiet, turbo)
                download_many(tracklist, quiet, False)
                print 'Finished Downloading: ',trackList
                main_cli(quiet, turbo)

            except KeyboardInterrupt:
                print '\nBye!'
                sys.exit()

        elif cmd_case.lower() in ['album', 'l']:
            try: 
                album = raw_input('Search for an album(^C to quit, ^B to return to menu): ')
                artist = raw_input('Artist of the album(^C to quit, ^B to return to menu): ')

                if album in ['^B', ''] or artist in ['^B', '']:
                    main_cli(quiet, turbo)

                trackList = get_tracks_by_album(artist, album)

                if not len(trackList):
                    print "No Tracks found"
                    main_cli(quiet, turbo)

                if turbo and not quiet:
                    print 'turbo is on, please wait a moment before continuing and press `Enter` when the proccess finishes'
                download_many(trackList, quiet, turbo)
                print 'Finished Downloading: ',trackList
                main_cli(quiet, turbo)

            except KeyboardInterrupt:
                print '\nBye!'
                sys.exit()

        elif cmd_case.lower() in ['track', 's']:
            try:
                track = raw_input('Search for a track(^C to quit, ^B to return to menu): ')

                if track in ['^B', '']:
                    main_cli(quiet, turbo)

                trackUrl = get_single_video_link(track)
                download_direct(trackUrl, quiet, turbo)
                main_cli(quiet, turbo)

            except KeyboardInterrupt:
                print '\nBye!'
                sys.exit()

        elif cmd_case.lower() in ['exit', 'quit', 'x']:
            print 'Bye!'
            sys.exit()

        elif cmd_case.lower() in ['turbo', 'zoom']:
            if turbo == True:
                turbo = False
                print 'Turned turbo off'
                main_cli(quiet, False)
            else:
                turbo = True
                print 'Turned turbo on'
                main_cli(quiet, True)

        elif cmd_case.lower() in ['quiet', 'shh', 'q']:
            if quiet == True:
                quiet = False
                print 'Turned quiet off'
                main_cli(False, turbo)
            else:
                quiet = True
                print 'Turned quiet on'
                main_cli(True, turbo)

        else:
            print 'Please enter a valid command or \'help\' for a list of commands'
            main_cli(quiet, turbo)
            
    if not sys.argv[1:]:
        main_cli(False, False)

    # TODO make a cli direct interface
    #  if not search_uses_flags(argument_string, '-a', '-l', '-t', '-q', '-T'):
        #  search = qp(' '.join(sys.argv[1:]))
        #  trackUrl = get_single_video_link(search)
        #  download_direct(trackUrl, False, False)

    #  if search_uses_flags(argument_string, '-q'):
        #  quiet = True
    
    #  if search_uses_flags(argument_string, '-T'):
        #  turbo = True

def search_uses_flags(argstring, *flags):
    """
    Check if the given flags are being used in the command line argument string
    """
    for flag in flags:
        if (argstring.find(flag) != 0):
            return True
    return False

    

def download_many(trackList, quiet, turbo):
    urls = []
    for track in trackList:
        urls.append(get_single_video_link(track))

    for url in urls:
        download_direct(url, quiet, turbo)

def tracks_from_artist(artist):
    """
    Query last.fm for an artist and return a list of tracks
    """
    albums = get_albums_by_artist(artist)

    albumTracks = []
    for album in albums:
        albumTracks.append(get_tracks_by_album(artist, album))
    allTracks = [item for sublist in albumTracks for item in sublist]   
    
    return allTracks

def get_video_list(query):
    """
    Makes a query to youtube and returns a list of the tracks that it finds and returns the object with the details

    :returns: list of videos with title and video link
    :rtype: list
    """
    found = search_videos(query)
    if not found:
        print "No videos found matching: " + query
    else:
        return found

def get_single_video_link(track):
    """
    Makes a query to youtube using a given track name + artist and returns the first track found from a youtube search

    :returns: a single video link to youtube '/watch?v=yqem6k_3pZ8'
    :rtype: unicode
    """
    found = search_videos(track)
    title, video_link = found[0]
    return video_link

def download_direct(url_path, quiet, turbo):
    """
    Download a track directly from the url
    Use with get_single_video(track)
    """
    command_tokens = [
        'youtube-dl',
        '--extract-audio',
        '--audio-format mp3',
        '--audio-quality 0',
        '--output \'%(title)s.%(ext)s\'',
        'https://www.youtube.com' + url_path]

    if turbo:
        command_tokens.append('&')

    if quiet:
        command_tokens.insert(1, '-q')

    command = ' '.join(command_tokens)

    # Youtube-dl is a proof that dog exists.
    os.system(command)
 
def makeRequest(url, hdr):
    """ Make HTTP requests to youtube """
    http_proxy  = os.environ.get("HTTP_PROXY")
    https_proxy = os.environ.get("HTTPS_PROXY")
    ftp_proxy   = os.environ.get("FTP_PROXY")

    proxyDict = { 
        "http"  : http_proxy,
        "https" : https_proxy,
        "ftp"   : ftp_proxy
        }

    req = requests.get(url, headers=hdr, proxies=proxyDict)
    return req

def search_videos(query):
    """
    Searches for videos given a query
    :rtype: list[tuple]
    """
    response = makeRequest('https://www.youtube.com/results?search_query=' + query, {})
    return extract_videos(response.content)

def list_movies(movies):
    """
    :rtype: generator object
    """
    for idx, (title, _) in enumerate(movies):
        yield '[{}] {}'.format(idx, title.decode('utf-8').encode(sys.stdout.encoding))


def extract_videos(html):
    """
    Parses given html and returns a list of (Title, Link) for
    every movie found.
    :returns: list of titles and links to videos
    :rtype: list[tuple]
    """
    soup = BeautifulSoup(html, 'html.parser')
    pattern = re.compile(r'/watch\?v=')
    found = soup.find_all('a', 'yt-uix-tile-link', href=pattern)
    return [(x.text.encode('utf-8'), x.get('href')) for x in found]

def get_albums_by_artist(artistQuery):
    """
    Get all albums for an artist based on a search query for the artist
    :returns: list of album names from search query
    :rtype: list[str]
    """
    artist = urllib.urlencode({ 'artist' : artistQuery })
    # make a query to the last.fm api for artists that match the artistQuery
    artistUrl = BASE_URL + '/2.0/?method=artist.gettopalbums&' + artist +'&api_key=' + API_KEY + '&format=json'

    # read the results of the query and convert to json
    artistAlbums = json.loads(urllib2.urlopen(artistUrl).read())

    albums = artistAlbums['topalbums']['album']
    albumNames = []
    for album in albums:
        # convert the album names from unicode and append to list 
        albumNames.append(unicorn.normalize('NFKD', album['name']).encode('ascii','ignore'))

    return albumNames

def get_tracks_by_album(artistQuery, albumQuery):
    """
    Get all tracks for an album based on a search query for the album
    :returns: tracklist from search query
    :rtype: list[str]
    """

    artist = urllib.urlencode({ 'artist' : artistQuery })
    album = urllib.urlencode({ 'album' : albumQuery })

    # query last.fm for album info
    albumInfo = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=' + API_KEY + '&' + artist + '&' + album + '&format=json'

    # read results of query and convert to json
    albumInfo = json.loads(urllib2.urlopen(albumInfo).read())['album']['tracks']['track']

    trackList = []
    for track in albumInfo:
        # convert track names from unicode and append to list
        trackList.append(artistQuery + ' - ' + unicorn.normalize('NFKD',track['name']).encode('ascii', 'ignore'))

    return trackList
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nBye!'
        sys.exit()

