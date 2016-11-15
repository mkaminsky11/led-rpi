import subprocess

def get():
	ret = subprocess.Popen(['hostname','-I'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0].strip().decode().split(" ")
	for r in ret:
		if r.index("18.") == 0: # mit ip address and stuff
			return r
	return None