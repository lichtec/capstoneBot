import os
#from sys import argv

def Ping(dest_addr, count):
	pingCmd='ping -c%s %s > /dev/null 2>&1' % (count, dest_addr)
	os.system(pingCmd)
	print('\nDone')
	exit()
