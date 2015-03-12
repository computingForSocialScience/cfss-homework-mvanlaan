from bs4 import BeautifulSoup
from io import open
from datetime import datetime
import time
import re
import sys
import grequests

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID."""
    url = "https://api.spotify.com/v1/search?q="+ name +"&type=artist"  
    req = grequests.get(url)
    result_list = grequests.map([req])
    if not result_list[0].ok:
        print "Error"
    info = result_list[0].json()
    ID = info['artists']['items'][0]['id']
    return(ID)   
def fetchArtistInfo(artist_id):
    url = "https://api.spotify.com/v1/artists/" + artist_id
    req = grequests.get(url)
    result_list = grequests.map([req])
    info = result_list[0].json()
    data = {}
    data['followers'] = info['followers']['total']
    data['genres'] = info['genres']
    data['id'] = info['id']
    data['name'] = info['name']
    data['popularity'] = info['popularity']
    return (data)