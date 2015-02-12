import sys
from fetchArtistedited import fetchartistid, fetchArtistInfo
from fetchAlbumsfinal import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "artists are", artist_names
    fetchedalbums = []
    fetchedartists = []
    for artnam in artist_names:
        idnumber = fetchArtistId(artnam)
        artists.append(fetchArtistInfo(idnumber))
        albums = fetchAlbumIds(artnam)
        for album in albums:
            fetchedalbums.append(fetchAlbumInfo(album))
    writeAlbumsTable(albums)
    writeArtistsTable(artists)
    plotBarChart()
    

