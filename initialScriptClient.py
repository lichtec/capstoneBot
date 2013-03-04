#!/usr/bin/python
import socket
import sys
import datetime
import threading
from ping import Ping

exitFlag=0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
    	threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        threading.Thread.__init__(self)
    def run(self):
        print "Starting " + self.name + '\n'
        Ping(5)
        print "Exiting " + self.name + '\n'


#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
server_address = ('198.252.11.72', 35000)
#server_address = ('localhost', 4444)
#server_address = ('localhost', 35000)
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
	thread1 = myThread(1, "Thread-1", 1)
	#thread2 = myThread(2, "Thread-2", 2)

	# Start new Threads
	thread1.start()
	#thread2.start()

	print "Exiting Main Thread"
	
finally:
	print >>sys.stderr, '\nClosing Socket'
	soc.close()
