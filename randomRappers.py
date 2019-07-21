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


#Pull all of the artist's albums
sp_albums = sp.artist_albums(artist_uri, album_type='album')
#Creates empty list to hold song names and ID's
test = []
for i in range(len(sp_albums['items'])):
    test.append((re.sub(r"[\(\[].*?[\)\]]", "", sp_albums['items'][i]['name']), sp_albums['items'][i]['id']))
#pprint.pprint(album_names)
#pprint.pprint(album_uris)
print(test)
#album_id = sp_albums['items'][i]['uri']
#album_id = boot.split(':')[2]