def arrayToLines(data):
	ret = []
	for i in range(0,7):
		text = ""
		for item in data:
			text = text + item[i]
		ret.append(text)
	return ret[::-1]

def arrayRev(data):
	ret = []
	for i in range(0,7):
		text = ""
		for item in data:
			text = text + item[i]
		ret.append(text)
	return ret

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


led = open('/home/pi/Github/led-rpi/normalfont','r').read().strip().split("\n")
ledFont = {}
for line in led:
	line = line.split(" ")
	ledFont[line[0]] = line[1::]
ledFont_space = ["000","000","000","000","000","000","000"]

def normalLines(lines, max):
	line_length = len(lines[0])
	if line_length < max:
		diff = max- line_length
		for i in range(0,7):
			lines[i] = lines[i] + ("0" * diff)
	elif line_length > max:
		for i in range(0,7):
			lines[i] = lines[i][0:max]
	return lines

def join3Rows(row1, row2, row3):
	arr = []
	for i in range(0,7):
		arr.append(row1[i] + row2[i] + row3[i])
	return arr

def simulate(lines):
	for l in lines[::-1]:
		print(" ".join(l[0:180].split("0")))
	for l in lines[::-1]:
		print(" ".join(l[180:360].split("0")))
	for l in lines[::-1]:
		print(" ".join(l[360:540].split("0")))

def blank():
	return ["","","","","","",""]
