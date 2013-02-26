#!/usr/bin/python
from socket import *
import threading
import thread
import sys

def handler(clientsock,addr):
	while 1:
		data = clientsock.recv(BUFSIZ)
		if not data:
			break
        	msg = data
		clientsock.send(msg)
		print >>sys.stderr, '\nReceived: "%s"' % msg
	clientsock.close()

if __name__=='__main__':
	HOST = 'localhost'
	PORT = 35000
	BUFSIZ = 1024
	ADDR = (HOST, PORT)
	serversock = socket(AF_INET, SOCK_STREAM)
	print >>sys.stderr, 'Starting Up On: %s => Port: %s' % ADDR
	serversock.bind(ADDR)
	serversock.listen(2)

	while 1:
		print 'Waiting For Connections'
		clientsock, addr = serversock.accept()
		f=open('client_address_list','a')
		f.write(str(addr) + '\n')
		f.close()

		print 'Connection From: ', addr
		thread.start_new_thread(handler, (clientsock, addr))
