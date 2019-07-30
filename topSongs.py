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

username = input("What is your username?: ")
#Scope and Access Token
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
client_secret=client_secret, redirect_uri='http://localhost:8888/callback')

uri = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLRQDuF5jeBp'

def get_track_ids(username):
    username = username
    playlist_id = uri.split(':')[4]
    results = sp.user_playlist(username, playlist_id)
    song_ids = []
    for songs in results['tracks']['items']:
        song_ids.append(songs['track']['id'])
    return song_ids

song_ids = get_track_ids(username)
my_playlist_id = '0HdcafGAFDMbydy1LJPQWj'

#def add_tracks():
   #return sd
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, my_playlist_id, song_ids)
    print(results)
else:
    print("Can't get token for", username)

