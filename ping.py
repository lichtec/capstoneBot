#!/usr/bin/python
import os, sys

threadCount=10

def Ping(threadCount):
	pingAddress='127.0.0.1'
	#pingCmd='ping -c18 %s | grep "potato"' % pingAddress
	pingCmd='ping -c2 %s > /dev/null 2>&1' % pingAddress
	os.system(pingCmd)
	print('Good Job')
	exit()