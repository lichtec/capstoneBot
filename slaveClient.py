#!/usr/bin/python
import socket
import sys
import datetime
import time
from slaveping import Ping

my_address = socket.gethostbyname(socket.gethostname())

slave = 'slave'
global ipAdd
global numPing
ipAdd = '198.252.11.72'
numPing = 5
global ping_time_str

#datetime.datetime(curr_time.year, curr_time.month, curr_time.day,curr_time.hour, curr_time.minute)
#datetime.timedelta(x,x) #where x,x is desired time (day,hour,minute,second,etc)
#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
#server_address = ('198.252.11.72', 35000)
server_address = (my_address, 35000)
print >>sys.stderr, 'Connecting To: %s => Port: %s' % server_address
soc.connect(server_address)

try:
	#send data
	message = 'Client Hostname: ' + socket.gethostname() + '\n' + 'slave'
	print >>sys.stderr, '\nSending: "%s"' % message
	soc.sendall(slave)
		
	while True:
		ipAdd = soc.recv(150)
		numPing = soc.recv(150)
		ping_time_str = soc.recv(150)
		print >>sys.stderr, 'new ipaddress is  ', ipAdd
		print >>sys.stderr, 'number of pings  ', numPing
		print >>sys.stderr, 'time to spam  ', ping_time_str
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
			print >>sys.stderr, 'all done'
			break

