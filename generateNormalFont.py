def normFontChar(char):

	# if all starts with row or col
	atFront = -1
	atBack = -1
	for line in char:
		front = zeroesAtFront(line)
		back = zeroesAtFront(line[::-1])
		if atFront == -1 or front < atFront:
			atFront = front
		if atBack == -1 or back < atBack:
			atBack = back
	# make it so that 1 at back and front
	addToFront = 1 - atFront
	addToBack = 1 - atBack
	newChar = []
	for line in char:
		newChar.append(modifyLine(line,addToFront,addToBack))
	return newChar

def zeroesAtFront(line):
	zeroes = 0
	for c in line:
		if c == "0":
			zeroes = zeroes + 1
		else:
			break
	return zeroes

def modifyLine(line, addToFront, addToBack):
	if addToFront < 0:
		line = line[(addToFront * -1):]
	elif addToFront > 0:
		line = ("0" * addToFront) + line

	if addToBack < 0:
		line = line[:(addToBack * -1)]
	elif addToBack > 0:
		line = line + ("0" * addToBack)

	return line

led = open('ledFont','r').read().strip().split("\n")
ledFont = {}
for line in led:
	line = line.split(" ")
	ledFont[line[0]] = '\n'.join(normFontChar(line[1::][::-1]))

text = []
for key in ledFont:
	line = key + " " + " ".join(ledFont[key].split("\n"))
	text.append(line)
text = "\n".join(text)
f = open('normalfont','w')
f.write(text)