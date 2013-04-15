import socket
import httplib
#s = socket.socket()        
host = 'ArchMO16'
print(host)
port = 80
conn = httplib.HTTPConnection(host, port, source_address=('', 80))
conn.connect()

#s.connect((host, port, source_address=('', 80))
#print(s.recv(1024))
#s.close                     