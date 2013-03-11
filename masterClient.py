import socket
import sys
import time

#Create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_address = socket.gethostbyname(socket.gethostname())

print>>sys.stderr,'my ip is %s' %my_address

#Connect the socket to the port where the server is listening
#server_address = ('198.252.11.72', 35000)
server_address = (my_address, 35000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
soc.connect(server_address)

try:
    
	#send data
	message = 'master'
	print >>sys.stderr, 'sending "%s"' % message
	soc.sendall(message)
	time.sleep(2)
	print >>sys.stderr, 'sending new ip address'
	soc.sendall('198.252.11.72')
	time.sleep(2)
	print >>sys.stderr, 'sending number of pings'
	soc.sendall('4')

finally:
	print >>sys.stderr, 'closing socket'
	soc.close()
