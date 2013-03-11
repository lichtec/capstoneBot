#!/usr/bin/python
from socket import *
import threading
import thread
import sys
import time

master='master'
slave='slave'
global ipAdd
global numPing
ipAdd ='198.252.11.70'
numPing = 5

def handler(clientsock,addr):
	while 1:
			global ipAdd
			global numPing
			data = clientsock.recv(BUFSIZ)
				#		clientsock.send(msg)
			print >>sys.stderr, '\nReceived: "%s"' % data
			if data == master:
				ipAdd = clientsock.recv(BUFSIZ)
				print >>sys.stderr, 'new ipaddress is "%s" ' % ipAdd
				time.sleep(2)
				numPing = str(clientsock.recv(BUFSIZ))
				print >>sys.stderr, 'number of pings is "%s"' % numPing
				#clientsock.send('confirming ipaddress is "%s" ' % ipAdd)
				#clientsock.send('confirming number of pings is "%s" ' % numPing)
				break
			elif data == slave:
				clientsock.send(ipAdd)
				print >>sys.stderr, ipAdd
				time.sleep(2)
				clientsock.send(str(numPing))
				print >>sys.stderr, numPing
				time.sleep(2)
				break
			else:
				print >>sys.stderr, 'invalid access from ', clientsock
				break
	print '\nWaiting For Connections'
	clientsock.close()

if __name__=='__main__':
	#HOST = 'localhost'
	#HOST = '198.252.11.72'  USE THIS
	HOST = '172.18.65.25'
	PORT = 35000
	BUFSIZ = 1024
	ADDR = (HOST, PORT)
	serversock = socket(AF_INET, SOCK_STREAM)
	print >>sys.stderr, 'Starting Up On: %s => Port: %s' % ADDR
	print 'Waiting For Connections'
	serversock.bind(ADDR)
	serversock.listen(2)

	while 1:
		clientsock, addr = serversock.accept()
		f=open('client_address_list','a')
		f.write(str(addr) + '\n')
		f.close()

		print '\nConnection From: ', addr
		thread.start_new_thread(handler, (clientsock, addr))

