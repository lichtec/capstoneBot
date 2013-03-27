from punch import *
import os

def Punch(serv_addr, dest_addr):
	punchCmd= 'punch -s %s -d %s -P1- -f' % (serv_addr, dest_addr)
	os.system(punchCmd)
	print('Done')
	exit()
