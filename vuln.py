'''CREATED BY MUHAMMAD HANAN ASGHAR'''
#!/usr/bin/python3

import socket
import os
import sys


def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		sock = socket.socket()
		sock.connect((ip,port))
		banner = sock.recv(1024)
		return banner
	except:
		return


def checkVulns(banner,filename):
	f = open(filename,"r")
	for line in f.readlines():
		if line.strip('\n') in banner:
			print("[+] Server is Vulnerable: " + "banner.strip('\n')")

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print('[-] File Doesnt Exist!')
			exit(0)
		if not os.access(filename, os.R_OK):
			print('[-] Access Denied!')
			exit(0)
	else:
		print(f'[-] Usage: {sys.argv[0]} <vuln filename>')
		exit(0)
	portlist = [22,21,25,80,110,443,445,135]
	for x in range(16,37):
		ip = f"192.168.1.{x}"
		for port in portlist:
			banner = retBanner(ip,port)
			if banner:
				print(f"[+] {ip}/{port} : {banner}")
				checkVulns(banner, filename)
main()
