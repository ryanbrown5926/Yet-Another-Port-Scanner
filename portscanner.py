
import socket #library to comunicate with other machines using TCP/UDP
#import termcolor #print statements in different colors

def scan(target, ports):
	for port in range(1,ports):
		scan_port(target, port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket() #socket initiator
		sock.connect((ipaddress, port)) #connect
		print("[+] port opened " + str(port))
		sock.close()
	except:
		print("[-] port closed" + str(port))

targets = input("[*] Enter targets to scan(split the by commas : ") #192.168.1.1, 192.168.1.5
ports = int(input("[*] Enter how many ports you want to scan: "))

if ',' in targets:
	print("[*] Scanning multiple targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)
