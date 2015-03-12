from flask import Flask, render_template, request, redirect, url_for
import pymysql
import unicodecsv
import sys
import requests
import networkx as nx
import pandas as pd
import random
from io import open
from artistNetworks import getEdgeList
from analyzeNetworks import randomCentralNode,pdToNX, combineEdgeLists 
from fetchArtists import *
from fetchAlbums import * 
app = Flask(__name__)
dbname="playlists"
host="localhost"
user="root"
passwd="mvanlaan"
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
def createNewPlaylist(ArtistName):
    c = db.cursor()
    make_table_playlists = '''create table playlists (id INTEGER PRIMARY KEY AUTO_INCREMENT, \rootArtist VARCHAR(128));'''
    make_table_songs = '''create table songs (playlistId INTEGER, \songOrder INTEGER, \artistName VARCHAR(128), \albumName VARCHAR(256), \trackName VARCHAR(256));'''                                                                                                                  
    c.execute(make_table_playlists)
    c.execute(make_table_songs)
    depth = 2
    edge_list = getEdgeList(artists_id,depth)
    artists_id = fetchArtistId(ArtistName)
    random_artists = []
    i = 30
    while i != 0:
        random_artist = randomCentralNode(pdToNX(edge_list))
        album_id_list = fetchAlbumIds(random_artist)
        random_artists.append(random_artist)
        i = i -1
    artist_names = []
    album_list = []
    for artist_id in random_artists:
        artist = fetchArtistInfo(artist_id)
        artist_name = artist['name']
        artist_names.append(artist_name)
        album_id_list = fetchAlbumIds(artist_id)
        random_album = (random.choice(album_id_list))
        random_album_info = fetchAlbumInfo(random_album) 
        random_album_name = random_album_info['name']
        newtuple = (random_album_name, random_album)
        album_list.append(newtuple)
    random_track_list = []
    for album in album_list:
        url = 'https://api.spotify.com/v1/albums/' + album[1] + '/tracks'
        req = requests.get(url)
        if req.ok == False: 
            print "Error"
        req.json()
        jsondata = req.json()
        info = jsondata.get('items')
        track_list = []
        for i in range(len(info)):
            track_name = info[i]['name']
            track_list.append(track_name)
            random_track = (random.choice(track_list))
        random_track_list.append(random_track)
    artist_name_in = """insert into playlists (rootArtist) VALUES ('%s')""" % (ArtistName)
    c.execute(artist_name_in)
    com_play = """select max(id) from playlists;"""
    c.execute(com_play)
    playlistId = c.fetchall()
    playlistId = playlistId[0][0]
    for i in range(len(random_track_list)):
        songOrder = i+1
        Artist_Name = '"' + artist_names[i] + '"'
        Artist_Name.replace('\'', "")
        Album_Name = '"' + album_list[i][0] + '"'
        Album_Name.replace('\'', "")
        Track_Name = '"' + random_track_list[i] + '"'
        Track_Name.replace('\'', "")
        sql = """insert into songs (playlistId, songOrder, artistName, albumName, trackName) VALUES (%s, %s, %s, %s, %s)""" % (playlistId, songOrder, Artist_Name, Album_Name, Track_Name)
        c.execute(sql)
        db.commit()
    c.close()
@app.route('/')
def make_index_resp():
    return(render_template('index.html'))
@app.route('/playlists/')
def make_playlists_resp():
    c = db.cursor()
    get_playlists = """select * from playlists;"""
    return render_template('playlists.html',playlists=playlists)
    c.execute(get_playlists)
    playlists = c.fetchall()
@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    c = db.cursor()
    input_playlist = playlistId
    song_request = """select songOrder, artistName, albumName,trackName FROM songs WHERE playlistId = (%s)""" % (input_playlist)
    c.execute(song_request)
    songs = c.fetchall()
    return render_template('playlist.html',songs=songs)
@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        artistName = request.form['artistName']
        createNewPlaylist(artistName)
        return(redirect("/playlists/"))
if __name__ == '__main__':
    app.debug=True
    app.run()
    for a in range(30):
            artist = random.choice(df)
            info = fetchArtistInfo(artist[1])
            artistName = info['name'].replace("'","''")
            related_artist = artist[1]
            album_list = fetchAlbumIds(artist[1])
	    songorder = a+1
            trackinfo = (playlist_id, songorder, artistName, album_name, song)
            song_list.append(trackinfo)
    insertion = '''insert into songs (playlistId, songorder, artistName, albumName, trackName) VALUES (%s, %s, %s, %s, %s);'''
    c.executemany(insertion,song_list)
db.commit()
if __name__ == '__main__':
    app.debug=True
    app.run()
