#import serial
#ser = serial.Serial('/dev/ttyACM0', 115200)

# ser.write('3')
# row | col on|off
# row: num col: pin on|off .... or .... all on .... or .... all on

#
#  6 * 30 * 3
#
#
#
#
rows = 7
cols = 540 # cutoffs: 0-179 180-359 360-539

# !
# -> {
#
#   "!": ["1","1","1","0","1"]
#
#
# }
#

#def diff(newState):
	#

#def unwrap(text):
	#

def arrayToSingleBlock(data):
	text = ""
	for i in range(0,7):
		for item in data:
			text = text + item[i]
		text = text + "\n"
	return text;

def textToFont(text):
	ret = []
	for char in text:
		if char in ledFont:
			# :)
			ret.append(ledFont[char])
		else:
			if char == " ":
				ret.append(ledFont_space)
	return ret


led = open('normalfont','r').read().strip().split("\n")
ledFont = {}
for line in led:
	line = line.split(" ")
	ledFont[line[0]] = line[1::]
ledFont_space = ["000","000","000","000","000","000","000"]

current_state = []
default_state = []
for i in range(0,rows):
	row = []
	for j in range(0,cols):
		row.append(False)
	current_state.append(row)
	default_state.append(row)

print(arrayToSingleBlock(textToFont("Hello world!")))