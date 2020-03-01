#!/usr/bin/env python3.7
import socket,concurrent.futures,sys

TIMEOUT = 1.5 # Change it if you want

def isAlive(childId,host):
	try:
		isAlive = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		isAlive.settimeout(TIMEOUT)
		notDead = isAlive.connect_ex((host, port)) == 0
		isAlive.close()
	except:
		notDead = False
	if notDead:
		print(host+"is open with "+port)
	else:
		print(host+"is closed with "+port)

if __name__ == "__main__":

	if len(sys.argv) < 4:
		print("Note: DON'T WRITE [ https:// and http:// and end-slash ! just the hostnames enough]\nUsage : python isAlive.py [hostList] [portRange] [Threads]\nex: python isAlive.py Hosts.txt 1-500 30")

	hostFile = sys.argv[1]
	portRange = sys.argv[2].split('-')
	threads = sys.argv[3]
	
	Hosts = open(hostFile,'r').read().splitlines()
	with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as pool_executor:
		for host in Hosts:
			for port in range(int(portRange[0]),int(portRange[1])):
				pool_executor.submit(isAlive, 0, host, port)
