from time import sleep
import sys
import time
import serial
from time import sleep

#**********
# UTILITIES
#**********
import font
import generator
import ip
import music

rpi = True
ser = None

if rpi:
	ser = serial.Serial('/dev/ttyACM0', 9600)

def send(lines):
	#print(lines)
	#font.simulate(lines)
	print("printing")
	ser.write("S".encode())
	for i in range(0,7):
		l = lines[i][::-1]
		#print(len(l))
		if i < 6:
			l = l + "\n"
		ser.write(l.encode())
	ser.write("E".encode())
	
def sendCol(col, state):
	#print("sending col")
	ser.write(("C" + str(col) + "\n"+ str(state) + "E").encode())


store_title = ""
store_playlist = ""
store_per = 0

ip_addr = ip.get()
line_1  = font.normalLines(font.arrayToLines(font.textToFont(ip_addr)), 191)
line_2  = font.normalLines(font.arrayToLines(font.textToFont("FUCK, THIS TOOK WORK")), 192)
line_3  = font.normalLines(font.arrayToLines(font.textToFont("WOAH PUTZ!")), 191)

lines = font.normalLines(font.join3Rows(line_1,line_2,line_3), 575)

sleep(5)

send(lines)

sleep(5)

while True:
	music_data = music.getData()

	title = music_data["song"]
	playlist = music_data["playlist"]
	per = music_data["per"] # % done

	if title != store_title:
		#print(title)
		#print(playlist)
		#print(per)
		title_lines = font.normalLines(font.arrayToLines(font.textToFont(title)), 191)
		playlist_lines = font.normalLines(font.arrayToLines(font.textToFont(playlist)), 192)
		length_lines = font.normalLines(generator.makeBar(per, 192),192)
		lines = font.normalLines(font.join3Rows(title_lines,playlist_lines,length_lines), 575)
		send(lines)
	#else:
		#
		#   186 = 100
		#   ____  
		#   cols   per
		#
		#
		#
		#
	old_num_bars = int(store_per * (186 / 100))
	new_num_bars = int(per * (186/ 100))

	if old_num_bars > new_num_bars:
		# remove all of the offending cols
		#diff = old_num_bars - new_num_bars
		# from 188
		for i in range(188 - old_num_bars, 188 - new_num_bars):
			# remove i
			sendCol(i, 0)
	elif new_num_bars > old_num_bars:
		# add new cols
		#diff = new_num_bars - old_num_bars
		# from 188
		for i in range(188 - new_num_bars, 188 - old_num_bars):
			# add i
			sendCol(i, 1)

	store_title = title
	store_playlist = playlist
	store_per = per


	sleep(3)

send(lines)
