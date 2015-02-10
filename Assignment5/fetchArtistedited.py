import sys
import requests
import json

name = 'Beck'

def fetchartistid(name):
    url = 'https://api.spotify.com/v1/search?q=' + name + '&type=artist'
    req = requests.get(url)
    if not req.ok:
    	print "Error"
    dct = req.json()
    assert dct.get('artists').get('items')
    id = dct['artists']['items'][0]['id']
    return id

fetchartistid(name)

def fetchArtistInfo(id):

    url = 'https://api.spotify.com/v1/artists/' + id
    req = requests.get(url)
    if not req.ok:
	print "Error"
    dct = req.json()
    info = {}
    assert dct.get('name')
    info['popularity'] = dct['popularity']
    info['followers'] = dct['followers']['total']
    info['name'] = dct['name']
    info['genres'] = dct['genres']
    info['id'] = id
    return info

id = fetchartistid(name)
print(fetchArtistInfo(id))





