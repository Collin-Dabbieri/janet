import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
from secrets import client_id
from secrets import client_secret

search_str='The Beatles'

scope = "app-remote-control,streaming,user-read-playback-state,user-modify-playback-state,user-read-currently-playing"
redirect_uri='https://www.google.com/'

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=scope))

# Search for a song
#result = sp.search(search_str)

results=sp.search(q='artist:' + search_str, type='artist')
uri=results['artists']['items'][0]['uri']
print(uri)

#pprint.pprint(result)
#print(result['tracks'].keys())

# Play that song
sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])
