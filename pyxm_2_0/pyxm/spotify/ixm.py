#!/usr/local/bin/python
# PyXm -IXM download functions
# Author : Edward Vetter-Drake
# Version : 1.2
import os, requests, re, sys, urllib2, json, subprocess
from bs4 import BeautifulSoup as YumSauce
from urllib import quote_plus as quip

import search

def main():
    #  download_direct([0,'yBuub4Xe1mw'], 'Led Zeppelin - Black Dog')
    #  print (search_videos('Led Zeppelin - Black Dog'))
    pass

def search_videos(query):
    """
    Searches for videos given a query
    :rtype: list[tuple]
    """
    response = makeRequest('https://www.youtube.com/results?search_query=' + query, {})
    return extract_videos(response.content)


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

def extract_videos(html):
    """
    Parses given html and returns a list of (Title, Link) for
    every movie found.
    :returns: list of titles and links to videos
    :rtype: list[tuple]
    """
    soup = YumSauce(html, 'html.parser')
    pattern = re.compile(r'/watch\?v=')
    found = soup.find_all('a', 'yt-uix-tile-link', href=pattern)
    return [(x.text.encode('utf-8'), x.get('href')) for x in found]

def list_movies(movies):
    """
    :rtype: generator object
    """
    for idx, (title, _) in enumerate(movies):
        yield '[{}] {}'.format(idx, title.decode('utf-8').encode(sys.stdout.encoding))

def download_direct(url_path, filename, quiet=False, turbo=False):
    """
    Download a track directly from the url
    """

    # for subprocess.call to work, each argument must be passed separately and in order
    command_tokens = [
        'youtube-dl',
        '--no-warnings',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '0',
        '--output', str(filename) + '.%(ext)s',
        '--no-playlist',
        'https://www.youtube.com' + str(url_path[1])
    ]

    if turbo:
        command_tokens.append('&')

    if quiet:
        command_tokens.insert(1, '-q')

    # Youtube-dl is a proof that doge exists.
    subprocess.call(command_tokens)
    return


if __name__ == '__main__':
    main()
