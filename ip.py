import subprocess

def get():
	ret = subprocess.Popen(['hostname','-I'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0].strip().decode().split(" ")
	for r in ret:
		if "18" in r: # mit ip address and stuff
			return r
	return "127.0.0.1"