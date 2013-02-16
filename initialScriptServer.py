#!/usr/bin/python
import socket
import sys

#create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind the socket to the port
server_Add = ('198.252.11.72', 35000)
print >>sys.stderr, 'Starting Up On: %s => Port: %s' % server_Add
soc.bind(server_Add)

#Now listen for incoming connections
soc.listen(1)

while True:
	#Wait for a connection
	print >>sys.stderr, 'Waiting For Connections'
	connection, client_address = soc.accept()
	
	try:
		cAddr=client_address
		host=str(cAddr)
		#hostname=str(socket.gethostbyaddr(host[:-9][2:]))
		#print >>sys.stderr, 'Hostname:', hostname
   		f=open('client_address_list','a')
		f.write(str(cAddr) + '\n')
   		f.close()
		print >>sys.stderr, '\nConnection From:', client_address 
	
		#Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(150)
			print >>sys.stderr, '\nReceived: "%s"' % data
		
			if data:
				print >>sys.stderr,'\nSending Data Back To Client'
				connection.sendall(data)
			else:
				print >>sys.stderr, '\nNo More Data From: ', client_address
				break
			
	finally:
		#Clean up the connection
		connection.close()
