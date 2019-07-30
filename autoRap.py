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


def get_artists():
    number_artists = int(input('How many artists would you like to enter: '))
    all_artists = []
    for artist in range(number_artists):
        all_artists.append(input('Enter artist name: '))
    return all_artists
#print(all_artists)

def get_artist_ids(all_artists):
    artist_ids = []
    for artist in all_artists:
        results = sp.search(q='artist:'+ artist)
        artist_ids.append(results['tracks']['items'][0]['artists'][0]['uri'])
    return artist_ids

all_artists = get_artists()
artist_uri = get_artist_ids(all_artists)
temp_artist = artist_uri[0]

for item in artist_uri:
    artist_id = item.split(':')[2]
    print(artist_id)



#Pull all of the artist's albums
#sp_albums = sp.artist_albums(artist_uri, album_type='album')


'''
#Store artist's albums' names' and uris in separate lists
album_names = []
album_uris = []
for i in range(len(sp_albums['items'])):
    album_names.append(sp_albums['items'][i]['name'])
    album_uris.append(sp_albums['items'][i]['uri'])
'''




'''
def get_track_ids(username):
    username = username
    artist_id = uri.split(':')[4]
    results = sp.artist_playlist(username, artist_id)
    song_ids = []
    for songs in results['tracks']['items']:
        song_ids.append(songs['track']['id'])
    return song_ids
print(get_track_ids(username))


result = sp.search(q='artist:'+ 'Young Thug')

song_ids = []
for songs in result['tracks']['items']:
   # song_ids.append(songs['track']['id'])
   print(songs['album']['id'])
#print(song_ids)
#pprint.pprint(result['tracks']['items'][10]['album']['id'])
'''