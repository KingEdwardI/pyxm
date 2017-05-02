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
        'bin/pyxm.py',
        'bin/menu.py',
        'bin/spotify/download.py',
        'bin/spotify/ixm.py',
        'bin/spotify/search.py',
        'bin/metadata/folders.py',
        'bin/metadata/id3tags.py',
        ],
    install_requires=[
        'youtube-dl',
        'BeautifulSoup4',
        'requests',
        'eyed3',
        'spotipy',
        'docopt'
        ],
    zip_safe=False,
    test_suite='nose2.collector.collector'
)
