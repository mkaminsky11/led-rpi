import subprocess

def get():
	ret = subprocess.Popen(['hostname','-I'], stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0].strip().decode().split(" ")
	#ret = subprocess.Popen(['ifconfig','wlan1','|','grep','"inet','addr:"'])
	#-> inet addr:18.111.92.166  Bcast:18.111.95.255  Mask:255.255.224.0
	_ip = []
	for r in ret:
		if "18" in r: # mit ip address and stuff
			_ip.append(r)
	return " ".join(_ip)
