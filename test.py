import httplib
import threading

# class threadClass(threading.Thread):
# 	def __init__(self, threadID, name, counter):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter
# 	def run(self):
# 		test()

host = 'www.python.org'
port = 80
		
x=5
while(x>0):
	conn = httplib.HTTPConnection(host, port)
	conn.request("GET", "/index.html")
	r1 = conn.getresponse()
	print x, r1.status, r1.reason, r1.msg
	x=x-1
	
# thread1 = threadClass(1, "Thread-1", 1)
# thread2 = threadClass(2, "Thread-2", 2)
# 
# thread1.start()
# thread2.start()
# 
# threads.append(thread1)
# threads.append(thread2)
# 
# for t in threads:
# 	t.join()
# 
# print "Exiting Main Thread"
#                    