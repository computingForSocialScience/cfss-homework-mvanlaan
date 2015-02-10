import unicodecsv as csv
import matplotlib.pyplot as plt #imports matplot library to plot a chart

def getBarChartData():

    #getting data from csv files
    f_artists = open('artists.csv')#opens artists.csv
    f_albums = open('albums.csv')#opens artists.csv

    #assigning data to certain aspects of the csv's
    artists_rows = csv.reader(f_artists)#labels artist_rows as info in artists.csv 
    albums_rows = csv.reader(f_albums)#labels album_rows as info in albums.csv

    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

    artist_names = [] #creates list artist_names
    
    decades = range(1900,2020, 10) #range of possible decades(1900-2020, increments of 10)
    decade_dict = {} #new dictionary called decade_dict
    for decade in decades:
        decade_dict[decade] = 0 #decade is the first entry
    
    for artist_row in artists_rows: #loops over the artist data
        if not artist_row:
            continue
        artist_id,name,followers, popularity = artist_row
        artist_names.append(name) #artist_id,name,followers, popularity are part of the artist_row data, attached to names

    for album_row  in albums_rows: #loops over the album data
        if not album_row: #doesn't apply if not in album data
            continue
        artist_id, album_id, album_name, year, popularity = album_row #artist_id, album_id etc. are part of album_row data
        for decade in decades:#loops over decades
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)): 
                decade_dict[decade] += 1 #adds decade to dictionary
                break 

    x_values = decades #x values are keys in dictionary
    y_values = [decade_dict[d] for d in decades] #y-values of bar chart will be the values in the new dictionary
    return x_values, y_values, artist_names 

def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData() #plots x values(decades), y values(albums), and artist_names 
    
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10) #sets width of bar to ten
    ax.set_xlabel('decades') #x axis is time, decade increments
    ax.set_ylabel('number of albums') #y axis is labeled number of albums
    ax.set_title('Totals for ' + ', '.join(artist_names)) #makes title depending on artist name and number of albums
    plt.show() #plots chart