import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
from spotify_secrets import client_id
from spotify_secrets import client_secret

genre='classical'
artist='The Beatles'
song='Here Comes The Sun'
album='Sleep Through The Static'
playlist='OA'
term='long_term'

scope = "user-top-read,app-remote-control,streaming,user-read-playback-state,user-modify-playback-state,user-read-currently-playing"
redirect_uri='https://www.google.com/'

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=scope))

def play_artist(artist):
	'''
	streams an artist's top songs
	'''

	results=sp.search(q='artist:' + artist, type='artist')
	# artist uri
	uri=results['artists']['items'][0]['uri']
	# artist's top tracks
	response=sp.artist_top_tracks(uri)
	# collect track uris
	uris=[track['uri'] for track in response['tracks']]
	# Play songs
	sp.start_playback(uris=uris)

def play_song(song):
	'''
	streams a song
	'''
	result=sp.search(q='track:'+song,type='track')
	uri=result['tracks']['items'][0]['uri']
	sp.start_playback(uris=[uri])

def play_album(album):
	'''
	streams an album
	'''
	results=sp.search(q='album:'+album,type='album')
	album_uri=results['albums']['items'][0]['uri']
	tracks=sp.album_tracks(album_uri)['items']
	uris=[track['uri'] for track in tracks]
	sp.start_playback(uris=uris)

def play_top_tracks(term):
	'''
	streams top tracks
	params:
		term - 'short_term', 'medium_term', or 'long_term'
	'''

	results=sp.current_user_top_tracks(time_range=term, limit=50)
	uris=[item['uri'] for item in results['items']]
	sp.start_playback(uris=uris)

def play_playlist(playlist):
	'''
	streams a playlist
	'''
	results=sp.search(q='playlist:'+playlist,type='playlist',limit=50)
	playlist_uri=results['playlists']['items'][0]['uri']
	tracks=sp.playlist_tracks(playlist_uri)['items']
	uris=[track['track']['uri'] for track in tracks]
	sp.start_playback(uris=uris)

def play_genre(genre):
	'''
	streams a genre
	'''
	#available_genres=sp.recommendation_genre_seeds()
	#print(available_genres)
	recommendations=sp.recommendations(seed_genres=[genre])['tracks']
	uris=[i['uri'] for i in recommendations]
	sp.start_playback(uris=uris)

def recommend_artist(artist):
	'''
	streams songs similar to an artist
	'''
	results=sp.search(q='artist:' + artist, type='artist')
	# artist uri
	artist_uri=results['artists']['items'][0]['uri']
	recommendations=sp.recommendations(seed_artists=[artist_uri])['tracks']
	uris=[i['uri'] for i in recommendations]
	sp.start_playback(uris=uris)

def recommend_song(song):
	'''
	streams songs similar to a song
	'''
	result=sp.search(q='track:'+song,type='track')
	song_uri=result['tracks']['items'][0]['uri']
	recommendations=sp.recommendations(seed_tracks=[song_uri])['tracks']
	uris=[i['uri'] for i in recommendations]
	sp.start_playback(uris=uris)

if __name__=='__main__':

	#play_artist(artist)
	#play_song(song)
	#play_album(album)
	#play_top_tracks(term)
	#play_playlist(playlist)
	#play_genre(genre)
	#recommend_artist(artist)
	recommend_song(song)
