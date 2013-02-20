import multiprocessing
import socket
import sys
import time
import os

#create a TCP/IP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_address = socket.gethostbyname(socket.gethostname())

#Bind the socket to the port
server_Add = (my_address, 8193)
print >>sys.stderr, 'starting up on %s port %s' % server_Add
soc.bind(server_Add)

#Now listen for incoming connections
soc.listen(1)

connNum=1
dataNum=1
  	
def server_conn(connNum, dataNum):	
	try:
		print >>sys.stderr, 'connection from', client_address
		#function junction
		while True:
			data = connection.recv(64)
			print >>sys.stderr, 'received "%s"' % data
			if data:
				print >>sys.stderr,'sending data back to the client'
				for j in range(4):
					connection.sendall('you are connection #' + str(connNum) + ' data # ' + str(dataNum))
					dataNum+=1
					print >>sys.stderr,'sending data# ',dataNum-1,' to connection # ', connNum
					time.sleep(2)			
				
				connection.sendall('dasEnde')
				connNum+=1
				dataNum=1
			else:
				print >>sys.stderr, 'no more data from', client_address
				break
	finally:
		connection.close()
							
if __name__ == "__main__":
#	print 'main pid', os.getpid()
	thread_list = []

	while True:
	#Wait for a connection
		print >>sys.stderr, 'waiting for a connection'
		connection, client_address = soc.accept()

		while connection:
			p = multiprocessing.Process(target=server_conn, args = (connNum,dataNum))
			p.start()
			p.join()
			thread_list.append(p)
			
	


