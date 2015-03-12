import numpy as np
import requests
from fetchArtists import fetchArtistId
from datetime import datetime
def fetchAlbumIds(artist_id):
    url = "https://api.spotify.com/v1/artists/"+artist_id+"/albums"\
    "?album_type=album&market=US"
    src = requests.get(url)
    album_data = src.json()
    albums = [album_data['items'][i]['id']\
    for i in range(len(album_data['items']))]
    return albums
def fetchAlbumInfo(album_id):
    album_dict = {}
    url = "https://api.spotify.com/v1/albums/"+album_id
    src = requests.get(url)
    album_data = src.json()
    album_dict['artist_id'] = album_data['artists'][0]['id']
    album_dict['album_id'] = album_data['id']
    album_dict['name'] = album_data['artists'][0]['name']
    album_dict['year'] = album_data['release_date'][0:4]
    album_dict['popularity'] = album_data['popularity']
    album_dict['album_name'] = album_data['name']
    return album_dict
def fetchRandomSong(album_id):
    url = "https://api.spotify.com/v1/albums/"+album_id+"/tracks"
    src = requests.get(url)
    album_data = src.json()
    track_names = []
    for i in range(len(album_data['items'])):
        track_names.append(album_data['items'][i]['name'])
    trackname = np.random.choice(track_names)
    return trackname