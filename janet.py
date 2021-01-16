import speech_recognition as sr
import pyttsx3
import sys
sys.path.append('./spotify/')
import stream_spotify as stream

listener=sr.Recognizer()


def take_command():

	activate=False
	while not activate:
		try:

			with sr.Microphone() as source:
				print('listening...')
				voice=listener.listen(source)
				command=listener.recognize_google(voice)
				command=command.lower()
				print(command)
				if 'hey janet' in command:
					activate=True
					# take string after activation phrase
					command=command.split('hey janet ',1)[1]
		except:
			pass

	return command

def run():
	command=take_command()
	print(command)

	# Handling Spotify Streaming Commands
	if 'list music commands' in command:
		print('listing music commands')
		print('play song')
		print('play album')
		print('play artist')
		print('play playlist')
		print('play top tracks')
		print('play genre')
		print('play songs like')
		print('play artists like')
	elif 'play song' in command:
		song=command.replace('play song ','')
		print('playing song '+song)
		stream.play_song(song)
	elif 'play album' in command:
		album=command.replace('play album ','')
		print('playing album '+album)
		stream.play_album(album)
	elif 'play artist' in command:
		artist=command.replace('play artist ','')
		print('playing artist '+artist)
		stream.play_artist(artist)
	elif 'play playlist' in command:
		playlist=command.replace('play playlist ','')
		print('playing playlist '+playlist)
		stream.play_playlist(playlist)
	elif 'play top tracks' in command:
		print('playing top tracks')
		stream.play_top_tracks('medium_term')
	elif 'play genre' in command:
		genre=command.replace('play genre ','')
		print('playing genre '+genre)
		stream.play_genre(genre)
	elif 'play songs like' in command:
		song=command.replace('play songs like ','')
		print('playing songs like '+song)
		stream.recommend_song(song)
	elif 'play artists like' in command:
		artist=command.replace('play artists like ','')
		print('playing artists like '+artist)
		stream.recommend_artist(artist)


while True:
	run()

