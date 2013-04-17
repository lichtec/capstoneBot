import os
#from sys import argv

def Hping(ipAdd, dest_addr):
	hpingCmd = 'sudo hping -i -u1 -S -p80 %s' % (dest_addr)
	os.system(hpingCmd)
	print('\nDone')
	exit()
