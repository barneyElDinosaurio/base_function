#-*-coding=utf-8-*-
import os,sys,subprocess
f=open('kill_id.txt')
data = f.readlines()
#print data
for i in data:
    kid= i.split()[1]
    os.system('kill %s' %kid)