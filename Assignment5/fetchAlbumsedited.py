import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
import sys

idnumb= '4NMPkMyu70G2MdDkP9zMAU'
def fetchAlbumIds(idnumb):
    url = 'https://api.spotify.com/v1/artists/' + idnumb + '/albums?market=US&album_type=album'
    req = requests.get(url)
    if not req.ok:
    	print "Error"
    req.json()
    data = req.json()
    getitems = data.get('items')
    albumids = []
    for i in range(len(getitems)):
    	getalbum = getitems[i]
    	getid = getalbum['id']
    	albumids.append(getid)
    return albumids

print fetchAlbumIds(idnumb)


idnumb= '1GjWNGbMtHDQ7CNYf2d7cw'
import csv

def fetchAlbumInfo(idnumb):  
    albuminfodict = {}  
    url = 'https://api.spotify.com/v1/albums/' + idnumb + '/albums?market=US&album_type=album'
    req = requests.get(url)
    if not req.ok:
    	print "Error"
    req.json()
    data = req.json()
    artistinfo = data.get('artists')
    artistid = artistinfo[0]['id']
    albumid = idnumb
    name = data.get('name')
    newdate = data.get('release_date')
    albumyear = newdate[0:4]
    albumpopularity = data.get('popularity')
    keys = ['artist_id', 'album_id', 'name', 'year', 'popularity']
    values = [get_artist_id, albumid, name, albumyear, albumpopularity]
    albuminfodict = dict(zip(keys,values))
    return albuminfodict
    

fetchAlbumInfo(idnumb)