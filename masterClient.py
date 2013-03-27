#!/usr/bin/python2
import socket
import sys
import time

#DATA ENTRY
#ipAddr = '198.252.11.72'
ipAddr = 'localhost'
nmPing = '4'
ping_time_str = "2013-03-13-13-39-0"

#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_address = socket.gethostbyname(socket.gethostname())

print>>sys.stderr,'My IP Address: %s' %my_address

#Connect the socket to the port where the server is listening
#server_address = ('198.252.11.72', 35000)
#server_address = (my_address, 35000)
server_address = ('localhost', 35000)
print >>sys.stderr, 'Connecting to: %s => Port: %s' % server_address
soc.connect(server_address)

try:
	#send data
	message = 'master'
	print >>sys.stderr, 'Sending: "%s"' % message
	soc.sendall(message)
	time.sleep(2)
	print >>sys.stderr, 'Sending New IP Address: %s' %ipAddr
	soc.sendall(ipAddr)
	time.sleep(2)
	print >>sys.stderr, 'Sending Number of Pings: %s' %nmPing
	soc.sendall(nmPing)
	time.sleep(2)
	print >>sys.stderr, 'Sending Ping Time: %s' %ping_time_str
	soc.sendall(ping_time_str)
	confirmIp = soc.recv(150)
	confirmPings = soc.recv(150)
	confirmPingTime = soc.recv(150)
	print >>sys.stderr, confirmIp
	print >>sys.stderr, confirmPings
	print >>sys.stderr, confirmPingTime

finally:
	print >>sys.stderr, 'Closing Socket'
	soc.close()
