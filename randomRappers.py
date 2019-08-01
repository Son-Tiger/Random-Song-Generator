import spotipy
import spotipy.util as util
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
import random
from random import sample
import re

#function to create playlist for listening music
def create_playlist(username, playlist_name):
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlists = sp.user_playlist_create(username, playlist_name)
        #pprint.pprint(playlists)
    else:
        print("Can't get token for", username)
    created_id = playlists['id']
    return created_id

#Gets artists from  user input
def get_artists(number_artists):
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

#Grabs list of albums from uris
def get_all_albums(artist_uri):
    all_artist_albums = [] #List of lists of all artist albums and ids
    #Pull all of the artist's albums
    for artist in range(len(artist_uri)):
        different_artist = [] # List of each artist's albums and ids
        sp_albums = sp.artist_albums(artist_uri[artist], album_type='album') #Artist Raw Information
        for i in range(len(sp_albums['items'])):
            different_artist.append((re.sub(r" [\(\[].*?[\)\]]", "", sp_albums['items'][i]['name']), sp_albums['items'][i]['id']))
        all_artist_albums.append(different_artist)
    return all_artist_albums

#Filters albums from list of all albums
def get_filter_albums(all_artist_albums):
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
    return filtered_albums

#Puts the filtered albums into updated list
def list_of_albums(filtered_albums):
    #Get a list of album songs
    artist_album_holder = []
    for musician in filtered_albums:
        each_artist = [] #List for each artist album
        for album in musician:
            album[1]#Album Ids
            each_artist.append(album[1])
        artist_album_holder.append(each_artist)
    return artist_album_holder

#Grabs a list of songs from updated list
def get_list_of_songs(artist_album_holder): #list of albums songs from each artist
    artist_tracks = []
    for artist in artist_album_holder: #List of list of albums
        tracks = []
        for albums in artist: #each album ID
            track = sp.album_tracks(albums) #pull data on album tracks
            for songs in track['items']: #songs from each album
                tracks.append(songs['id']) #add songs to song list
        artist_tracks.append(tracks) #adds album list to artist list
    return artist_tracks

#Puts the list of songs into a playlist holder
def playlist_album(artist_tracks, random_amount): #function to get random songs
    playlist = []
    for artist in artist_tracks:
        rand = sample(artist, random_amount)
        playlist.append(rand)
    #pprint.pprint(playlist)
    flat_list = []
    for sublist in playlist:
        for item in sublist:
            flat_list.append(item)
    return flat_list

#Feeds the playlist holder to function to create album
def your_album(username, playlist_id, random_playlist):
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, random_playlist)
    return results

if __name__ == '__main__':
    # Spotify Token/Info Access
    client_id = "9c815510a7a04bd69b5badfe865004f2"
    client_secret = "bc9da2b150a7461ba67b7990e0f59207"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    redirect_uri: "http://localhost:8888/callback"

    username = input("What is your username?: ")
    playlist_name = input("What would you like to name your playlist: ")

    #Scope and Access Token
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
    client_secret=client_secret, redirect_uri='http://localhost:8888/callback')

    #function to create playlist for listening music
    playlist_id = create_playlist(username, playlist_name)

    #Gets artists from  user input
    number_artists = int(input('How many artists would you like to enter: '))
    random_amount = int(input('How many songs from each artist would you like: '))
    all_artists = get_artists(number_artists)

    #Grabs artist uri from list of artists
    artist_uri = get_artist_uri(all_artists)

    #Grabs list of albums from uris
    all_artist_albums = get_all_albums(artist_uri)

    #Filters albums from list of all albums
    filtered_albums = get_filter_albums(all_artist_albums)

    #Puts the filtered albums into updated list
    artist_album_holder = list_of_albums(filtered_albums)

    #Grabs a list of songs from updated list
    artist_tracks = get_list_of_songs(artist_album_holder)

    #Puts the list of songs into a playlist holder
    random_playlist = playlist_album(artist_tracks, random_amount)

    #Feeds the playlist holder to function to create album
    your_album(username, playlist_id, random_playlist)