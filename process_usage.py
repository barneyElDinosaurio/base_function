# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import os
from multiprocessing import Process
def fork_case():
    print "Process %s start " %os.getpid()
    pid=os.fork()

    if pid==0:
        print "i am child process. and my parent pid is %s " %os.getpid()
    else:
        print "i am parent process %s, and create my child process %s" %(os.getpid(),pid)


def sub_proc():
    for i in range(10):
        print "under subprocess, parent pid %s" %os.getpid()

def process_testcase():
    print "parent process"
    print 'creating sub process'
    p=Process(target=sub_proc,args=())
    p.start()
    p.join()
    print 'done'

def main():
    #fork_case()
    process_testcase()
main()