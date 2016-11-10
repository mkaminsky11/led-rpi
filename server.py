import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

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

def diff(newState):
	#

def unwrap(text):
	#

def textToFont(text):
	#

led = open('normalfont','r').read().strip().split("\n")
ledFont = {}
for line in led:
	line = line.split(" ")
	ledFont[line[0]] = line[1::]

print(ledFont)

current_state = []
for i in rows:
	row = []
	for j in cols:
		row.append(False)
	current_state.append(row)