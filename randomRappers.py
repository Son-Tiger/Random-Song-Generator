import spotipy
import spotipy.util as util
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
import random
import re


# Spotify Token/Info Access
client_id = "9c815510a7a04bd69b5badfe865004f2"
client_secret = "bc9da2b150a7461ba67b7990e0f59207"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
playlist_id: "0HdcafGAFDMbydy1LJPQWj"
redirect_uri: "http://localhost:8888/callback"

#username = input("What is your username?: ")
username = 'twqfst'


#Scope and Access Token
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
client_secret=client_secret, redirect_uri='http://localhost:8888/callback')


#Gets artists from  user input
def get_artists():
    number_artists = int(input('How many artists would you like to enter: '))
    all_artists = []
    for artist in range(number_artists):
        all_artists.append(input('Enter artist name: '))
    return all_artists


#Grabs artist uri from list of artists
def get_artist_uri(all_artists):
    artist_ids = []
    for artist in all_artists:
        results = sp.search(q='artist:'+ artist)
        artist_ids.append(results['tracks']['items'][0]['artists'][0]['uri'])
    return artist_ids


#Sets functions to variables
all_artists = get_artists() #Sets get artist function to variable
artist_uri = get_artist_uri(all_artists) #Sets get artist id function to variable
#print(artist_uri) #Grabs Artist  URI


all_artist_albums = [] #List of lists of all artist albums and ids

#Pull all of the artist's albums
for artist in range(len(artist_uri)):
    different_artist = [] # List of each artist's albums and ids
    sp_albums = sp.artist_albums(artist_uri[artist], album_type='album') #Artist Raw Information
    for i in range(len(sp_albums['items'])):
        different_artist.append((re.sub(r" [\(\[].*?[\)\]]", "", sp_albums['items'][i]['name']), sp_albums['items'][i]['id']))
    all_artist_albums.append(different_artist)

filtered_albums = []
#Algorithim to remove duplicates
for person in all_artist_albums: #For each list in list of lists
    albums = []
    #Using set
    visited = set()
    # Iteration
    for a, b in person:
        if not a in visited:
            visited.add(a)
            albums.append((a, b))
    filtered_albums.append(albums)

#Get a list of album songs
artist_song_holder = []

for musician in filtered_albums:
    each_artist = [] #List for each artist album
    for album in musician:
        album[1]#Album Ids
        each_artist.append(album[1])
    artist_song_holder.append(each_artist)

pprint.pprint(artist_song_holder)


