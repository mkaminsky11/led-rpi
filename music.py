import json
from urllib.request import urlopen

jsonPath = 'http://nr.mit.edu/audio/json/controls_update/'

def getData():
	text = urlopen(jsonPath).read().decode('utf-8')
	data = json.loads(text)

	title =""
	if len(data["songs"]) > 0:
		title = data["songs"][0]
	song_complete_per = 100 * (data["elapsed_time"] / data["song_duration"])
	playlist_info = "■   0 songs (0 mins)" # 3 spaces
	if data["playing"] == True:
		playlist_info = "►   " + str(data["playlist_length"]) + " songs (" + str(int(data["playlist_duration"] / 60)) + " mins)"
	return {
		"song": title,
		"per": song_complete_per,
		"playlist": playlist_info
	}