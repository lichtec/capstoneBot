#!/usr/bin/python
import os, sys

pingAddress='172.18.69.236'
pingCmd='ping -c18 %s | grep "potato"' % pingAddress

os.system(pingCmd)
print('Good Job')
