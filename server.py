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

import wiringpi

SPIchannel = 1 #SPI Channel (CE1)
SPIspeed = 500000 #Clock Speed in Hz

'''
wiringpi.pinMode(6,1) # Set pin 6 to 1 ( OUTPUT )
wiringpi.digitalWrite(6,1) # Write 1 ( HIGH ) to pin 6
wiringpi.digitalRead(6) # Read pin 6

int wiringPiSPIDataRW (int channel, unsigned char *data, int len) ;
'''

# PINS: https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/2/4/header_pinout.jpg
latchPin = 12 # TODO: fix this!!!!!!!!!!!!
clockPin = 11 # TODO: fix this (?) 11 = GPIO11 = SPI_CLCK
			  	# GPIO10 = SPI_MOSI
			  # GPIO10 = SPI_MISO `
dataPin = 9 # TODO: fix this !!!!!!!!!!!
switchPin = 17 # GPIO 17 = GPIO_GEN0 .... connect other to ground (6)

rpi = False
ser = None

if rpi:
	ser = serial.Serial('/dev/ttyACM0', 38400)
	wiringpi.wiringPiSetupGpio()
	wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)
	wiringpi.pinMode(17,0)
	# if digitalRead(17) ... then high ... otherwise ... low (TODO: test this)

def send(lines):
	if rpi:
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
lines = font.normalLines(font.arrayToLines(font.textToFont("❤ ►" * 1)), 575)
font.simulate(lines)
'''

music_data = music.getData()

title = music_data["song"]
playlist = music_data["playlist"]
per = music_data["per"] # % done

title_lines = font.normalLines(font.arrayToLines(font.textToFont(title)), 180)
playlist_lines = font.normalLines(font.arrayToLines(font.textToFont(playlist)), 180)
length_lines = font.normalLines(generator.makeBar(per, 180),180)

lines = font.normalLines(font.join3Rows(title_lines,playlist_lines,length_lines), 575)
font.simulate(lines)

# print(ip.get())