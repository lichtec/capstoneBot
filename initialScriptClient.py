#!/usr/bin/python
import socket
import sys
import datetime
import threading
from ping import Ping

exitFlag=0
threadList=[]

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
    	threading.Thread.__init__(self)
        self.threadID = threadID
        print("Thread Name is " + self.name)
        self.name = name
        self.counter = counter
        threading.Thread.__init__(self)
    def run(self):
        print "Starting " + self.name + '\n'
        Ping(100)
        print "Exiting " + self.name + '\n'
i=1
while(i<120):
	threadList.append(str(i))
	i+=1

#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
#server_address = ('198.252.11.72', 35000)
#server_address = ('localhost', 4444)
server_address = ('localhost', 35000)
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
	
	threadID=1
	threads =[]
	
	for tName in threadList:
		print('tName: ' + tName)
		print('threadID: ' + str(threadID))
		thread = myThread(threadID, tName, threadID)
		print('Thread: ' + str(myThread))
		thread.start()
		threads.append(thread)
		threadID += 1


	print "Exiting Main Thread"
	
finally:
	print >>sys.stderr, '\nClosing Socket'
	soc.close()
