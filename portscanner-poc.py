#!/usr/bin/python3

import sys, socket, pyfiglet

ascii_banner = pyfiglet.figlet_format("Port Scanning is Not a Crime")
print(ascii_banner)

#ip = '10.0.0.8'
ip = '10.10.160.65' #[FIXME] HARDCODED FAST OPTION
# alternative way of grabbing address
#ip = socket.gethostbyname(host)
open_ports = []

ports = range(1,9999) #[FIXME] FAST OPTION
#ports = range(1, 65535)
# optional for fast scanning of common services
#ports2 = {21,22,23,53,80,135,443,445}

def probe_port(ip, port, result=1): # attempts to connect to ports
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((ip, port))
		if r == 0:
			result = r
		sock.close()
	except Exception as e:
		pass
	return result

# prints out open ports and append to array
for port in ports:
	sys.stdout.flush()
	response = probe_port(ip, port)
	if response == 0:
		open_ports.append(port)

