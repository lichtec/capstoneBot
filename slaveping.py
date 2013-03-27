import os
#from sys import argv

def Ping(dest_addr, count):
	pingCmd='ping -c%s %s > /dev/null 2>&1' % (dest_addr, count)
	os.system(pingCmd)
	print('Done')
	exit()
