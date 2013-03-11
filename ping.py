#!/usr/bin/python
import os, sys

threadCount=10

def Ping(pings):
	pingAddress='192.168.1.1'
	#pingCmd='ping -c18 %s | grep "potato"' % pingAddress
	pingCmd='ping -c%s %s > /dev/null 2>&1' % (pings, pingAddress)
	os.system(pingCmd)
	print('Good Job')
	exit()
