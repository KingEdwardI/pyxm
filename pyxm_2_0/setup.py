#!/usr/local/bin/python
from setuptools import setup
from sys import platform
setup(
    name='PyXm',
    version='2.0',
    description='Single or batch download of songs based on various queries',
    url='https://github.com/KingEdwardI/PyXm',
    author='Edward Vetter-Drake',
    author_email='edward.vetterdrake@gmail.com',
    packages=['pyxm'],
    scripts=[
        'pyxm/pyxm.py',
        'pyxm/menu.py',
        'pyxm/spotify/download.py',
        'pyxm/spotify/ixm.py',
        'pyxm/spotify/search.py',
        'pyxm/metadata/folders.py',
        'pyxm/metadata/id3tags.py',
        'pyxm/metadata/cleanup.py'
        ],
    install_requires=[
        'youtube-dl',
        'BeautifulSoup4',
        'requests',
        'eyed3',
        'spotipy',
        'docopt',
        'tqdm'
        ],
    zip_safe=False,
    test_suite='nose2.collector.collector'
)
