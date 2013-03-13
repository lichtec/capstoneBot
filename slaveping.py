import os
#from sys import argv

def Ping(dest_addr, count):
	os.system('traceroute %s' % dest_addr)