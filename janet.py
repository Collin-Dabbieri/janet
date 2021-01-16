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

	if 'play song' in command:
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
		stream.play_top_tracks('medium_term')


while True:
	run()

