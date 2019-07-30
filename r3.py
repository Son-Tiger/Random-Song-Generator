import spotipy
import spotipy.util as util
import pprint
from spotipy.oauth2 import SpotifyClientCredentials

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

name = "{Young Thug}" #chosen artist
result = sp.search(name) #search query
#Extract Artist's uri
artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
#Pull all of the artist's albums
sp_albums = sp.artist_albums(artist_uri, album_type='album')

#Store artist's albums and uris in separate lists
album_names = []
album_uris = []
#Appends albums and uri's to list
for i in range(len(sp_albums['items'])):
    album_names.append(sp_albums['items'][i]['name'])
    album_uris.append(sp_albums['items'][i]['uri'])

album_names
print(album_uris)


album = album_uris
spotify_albums[album] = {} #Creates dictionary for that specific album

'''
#Create keys-values of empty lists inside nested dictionary for album
spotify_albums[album]['album'] = [] #create empty list
spotify_albums[album]['track_number'] = []
spotify_albums[album]['id'] = []
spotify_albums[album]['name'] = []
spotify_albums[album]['uri'] = []
tracks = sp.album_tracks(album) #pull data on album tracks


spotify_albums = {}
album_count = 0


for n in range(len(tracks['items'])): #for each song track
    spotify_albums[album]['album'].append(album_names[album_count]) #append album name tracked via album_count
    spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
    spotify_albums[album]['id'].append(tracks['items'][n]['id'])
    spotify_albums[album]['name'].append(tracks['items'][n]['name'])
    spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])


for i in album_uris: #each album
    albumSongs = []
    albumSongs(i)
    print("Album " + str(album_names[album_count]) + " songs has been added to spotify_albums dictionary")
    album_count+=1 #Updates album count once all tracks have been added
'''