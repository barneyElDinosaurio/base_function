# -*-coding=utf-8-*-
__author__ = 'Rocky'
import os,re

cwd=os.getcwd()
p=re.compile('\.txt')
print cwd
for dirpath, dirname,filename in os.walk(cwd):
    #print dirpath,dirname,filename
    #print dirpath
    print dirname
    print type(filename)
    if filename is not None:
        for i in filename:
        #if filename is not None:

            if p.search(i):
                os.remove(os.path.join(dirpath,i))
