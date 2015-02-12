import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
import sys

idnumb= '1GjWNGbMtHDQ7CNYf2d7cw'
def fetchAlbumIds(idnumb):
    url = 'https://api.spotify.com/v1/artists/' + idnumb + '/albums?market=US&album_type=album'
    req = requests.get(url)
    if not req.ok:
    	print "Error"
    req.json()
    data = req.json()
    getitems = data.get('items')
    albumidnumbs = []
    for i in range(len(getitems)):
    	getalbum = getitems[i]
    	getid = getalbum['id']
    	albumidnumbs.append(getid)
    return albumidnumbs

print fetchAlbumIds(idnumb)


import csv

def fetchAlbumInfo(albumidnumb):  
    albuminfodict = {}  
    url = 'https://api.spotify.com/v1/albums/' + albumidnumb
    req = requests.get(url)
    if not req.ok:
    	print "Error"
    req.json()
    data = req.json()
    artistinfo = data.get('artists')
    artistid = idnumb
    albumid = fetchAlbumIds(idnumb)
    name = data.get('name')
    newdate = data.get('release_date')
    albumdate= newdate[:4]
    albumpopularity = data.get('popularity')
    keys = ['artist_id', 'album_id', 'name', 'year', 'popularity']
    values = [artistid, albumid, name, albumyear, albumpopularity]
    albuminfodict = dict(zip(keys,values))
    return albuminfodict
    

fetchAlbumInfo(albumidnumb)