import json
from urllib.request import urlopen

jsonPath = 'http://18.248.7.27:5000/audio/json/controls_update'
#jsonPath = 'http://nr.mit.edu/audio/json/controls_update/'

def getData():
	text = urlopen(jsonPath).read().decode('utf-8')
	data = json.loads(text)

	title =""
	if len(data["songs"]) > 0:
		title = data["songs"][0]
	song_complete_per = 0
	if data["song_duration"] != 0:
		song_complete_per = 100 * (data["elapsed_time"] / data["song_duration"])
	playlist_info = "|| 0 songs (0 mins)" # 3 spaces
	if data["playing"] == True:
		playlist_info = ">   " + str(data["playlist_length"]) + " songs (" + str(int(data["playlist_duration"] / 60)) + " mins)"


	if data["playing"] == False and len(data["songs"]) == 0:
		# nothing playing
		return {
			"song": "Nothing queued...",
			"per": 0,
			"playlist": "kmichael and shreyask"
		}

	return {
		"song": title,
		"per": song_complete_per,
		"playlist": playlist_info
	}
