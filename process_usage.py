# -*-coding=utf-8-*-
import random
import time

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import os
import multiprocessing
multiprocessing.freeze_support()
from multiprocessing import Process,Pool,Queue
def fork_case():
    #can't work under windows
    print "Process %s start " %os.getpid()
    pid=os.fork()

    if pid==0:
        print "i am child process %s. and my parent pid is %s " %(os.getpid(),os.getppid())
    else:
        print "i am parent process %s, and create my child process %s" %(os.getpid(),pid)

def pid_test():
    print 'pid ',os.getpid()
    print 'ppid ',os.getppid()

def sub_proc():

    for i in range(10):
        print "under subprocess, parent pid %s" %os.getpid()

    print "work"

def process_testcase():
    print "parent process"
    print 'creating sub process'
    p=Process(target=sub_proc,args=())
    p.start()
    p.join()
    print 'done'

def sub_pool(i):
    start=time.time()
    print '%d process %s start time: %s' %(i ,os.getpid(),start)
    time.sleep(3)
    end=time.time()
    print 'process  end time: ' ,end

def process_pool():
    p=Pool(10)
    start=time.time()
    print "main start ",start
    for i in xrange(10):
        p.apply_async(sub_pool,args=(i,))
    p.close()
    p.join()
    end=time.time()
    print "process done at ",end

def process_write(q):
    print 'write in queue'
    for i in 'Chinese World Wide':
        q.put(i)
        time.sleep(random.random()*5)

def process_read(q):
    print "read in queue"
    while 1:
        data=q.get(True)
        print "I get : ",data

def process_communication():
    q=Queue()
    pw=Process(target=process_write,args=(q,))
    pr=Process(target=process_read,args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    print "done"

def main():

    fork_case()
    #process_testcase()
    #process_pool()
    #process_communication()
    #pid_test()
if __name__=='__main__':
    main()