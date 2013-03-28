import os
#from sys import argv

def Punch(ipAdd, dest_addr):
	punchCmd= 'sudo ./punch -s %s -d %s -P1- -f > /dev/null 2>&1' % (ipAdd, dest_addr)
	os.system(punchCmd)
	print('\nDone')
	exit()
