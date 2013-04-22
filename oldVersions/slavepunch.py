import os
#from sys import argv

def Punch(ipAdd, dest_addr):
	# punchCmd= 'sudo ./punch -s %s -d %s -P1- -f > /dev/null 2>&1' % (ipAdd, dest_addr)
	punchCmd= 'sudo ./punch -s %s -d %s -P1- -f' % (ipAdd, dest_addr)
	#punchCmd = 'sudo ./punch -s %s -d %s -P1- -f -p'perl -e 'print "." x 1400'
	os.system(punchCmd)
	print('\nDone')
	exit()
