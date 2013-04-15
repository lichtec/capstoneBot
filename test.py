import httplib
host = 'ArchMO16'
port = 80
conn = httplib.HTTPConnection(host, port)
conn.request("Get", "/index.html")
r1 = conn.getresponse()
print r1.status, r1.reason                   
