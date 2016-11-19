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
	ser = serial.Serial('/dev/ttyACM0', 38400)

def send(lines):
	if rpi:
		print("printing")
		ser.write("S".encode())
	for i in range(0,7):
		l = lines[i][::-1]
		if i < 6:
			l = l + "\n"
		if rpi:
			ser.write(l.encode())
	if rpi:
		ser.write("E".encode())
	

#
# TESTING
#

'''
#lines = font.normalLines(font.arrayToLines(font.textToFont("❤ ►" * 1)), 575)
#font.simulate(lines)
'''

music_data = music.getData()

title = music_data["song"]
playlist = music_data["playlist"]
per = music_data["per"] # % done

title_lines = font.normalLines(font.arrayToLines(font.textToFont(title)), 180)
playlist_lines = font.normalLines(font.arrayToLines(font.textToFont(playlist)), 180)
length_lines = font.normalLines(generator.makeBar(per, 180),180)

lines = font.normalLines(font.join3Rows(title_lines,playlist_lines,length_lines), 575)
#print(lines)
send(lines)
#font.simulate(lines)

# print(ip.get())
