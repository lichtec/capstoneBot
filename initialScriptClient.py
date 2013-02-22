#!/usr/bin/python
import socket
import sys

#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
server_address = ('198.252.11.72', 35000)
#server_address = ('localhost', 4444)
print >>sys.stderr, 'Connecting To: %s => Port: %s' % server_address
soc.connect(server_address)

try:

	#send data
        message = 'Client Hostname: ' + socket.gethostname() + '\n' + 'This is the message. It will be repeated.'
	print >>sys.stderr, '\nSending: "%s"' % message
	soc.sendall(message)

	#Look for response
	amount_received = 0
	amount_expected = len(message)
	
	while amount_received < amount_expected:
		data = soc.recv(150)
		amount_received += len(data)
		print >>sys.stderr, '\nReceived: "%s"' % data
	
finally:
	print >>sys.stderr, '\nClosing Socket'
	soc.close()
