def makeBar(per, width):
	w = int((per/100) * (width - 8))
	blank = (width - 8) - w
	arr = []
	for i in range(0,7):
		line = "1100" + ("1" * w) + ("0" * blank) + "0011"
		arr.append(line)
	return arr