from setuptools import setup
from sys import platform
setup(
    name='PyXm',
    version='1.0',
    description='Single or batch download of songs based on various queries',
    url='https://github.com/KingEdwardI/PyXm',
    author='Edward Vetter-Drake',
    author_email='edward.vetterdrake@gmail.com',
    license='None',
    packages=['pyxm'],
    scripts=['bin/pyxm','bin/api_key.py.py'],
    install_requires=[
        'youtube-dl',
        'BeautifulSoup4',
        'requests'
        ],
    zip_safe=False,
    test_suite='nose2.collector.collector'
)
