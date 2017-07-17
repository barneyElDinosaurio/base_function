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
from multiprocessing import Process,Pool,Queue,Manager
#import Queue
manager=Manager()
q=manager.Queue()
lock=manager.Lock()
def fork_case():
    #can't work under windows
    print "Process %s start " %os.getpid()
    pid=os.fork()

    if pid==0:
        print "i am child process %s. and my parent pid is %s " %(os.getpid(),os.getppid())
    else:
        print "i am parent process %s, and create my child process %s" %(os.getpid(),pid)

def basic_usage():
    print 'pid ',os.getpid()
    #print 'ppid ',os.getppid()
    cpus = multiprocessing.cpu_count()
    print cpus

    name=multiprocessing.current_process().name
    print name

def single_task(i):
    print "%s: process: %s " %(time.time(),i)
    print multiprocessing.current_process().name
    time.sleep(50)
    print 'finish'

def main_process():
    print multiprocessing.current_process().name
    print "go to child process"
    for i in xrange(1000):
        p=Process(target=single_task,args=(i,))
        p.start()
        #p.join()
    print "End"

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

def sub_pool(q1):
    start=time.time()
    i=1
    print '%d process %s start time: %s' %(i ,os.getpid(),start)
    time.sleep(3)
    end=time.time()
    name=multiprocessing.current_process().name
    print name
    #print j
    time.sleep(1)
    q1.put(i)
    print 'process  end time: ' ,end

def process_pool():
    p=Pool(10)
    start=time.time()
    #q1=Queue.Queue()
    manager=Manager()
    q=manager.Queue()
    print "main start ",start
    for i in xrange(10):
        p.apply_async(sub_pool,args=(q,))
    p.close()
    p.join()
    end=time.time()

    print "process done at ",end
    #print q
    print q.get()
    '''
    while q1.empty() ==False:
        d= q1.get(True)
        print d
    '''

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


def single(n):
    time.sleep(1)
    return n*n

def pool_map():
    x=[i for i in range (50) if i%2==0]
    #print x

    start=time.time()
    '''
    for i in x:
        single(i)
    print "time used " , time.time()-start
    '''
    #using multiprocess
    p=Pool(2)
    s=p.map(single,x)
    p.close()
    p.join()
    print s
    print len(s)
    print "end. Time used: ",time.time()-start

def pool_write(q):
    lock.acquire()
    for i in "Chinese World wide":
        q.put(i)
        print "put in queue"
    print 'release'
    lock.release()


def pool_read(q):
    while True:
        if  not q.empty():

            print q.get(True)
            print "geting"
        else:
            break




def pool_lock():
    '''
    manager=Manager()
    q=manager.Queue()
    lock=manager.Lock()
    '''
    p=Pool()

    p.apply_async(pool_write,args=(q,lock))
    p.apply_async(pool_read,args=(q,))

    p.close()
    p.join()
    print "end"

def main():
    pass
    #fork_case()
    #process_testcase()
    #process_pool()
    #process_communication()
    #basic_usage()
    #main_process()
    #pool_map()
    #pool_lock()

if __name__=='__main__':
    #main()
    '''
    manager=Manager()
    q=manager.Queue()
    lock=manager.Lock()
    '''
    p=Pool()

    p.apply_async(pool_write,args=(q,))
    p.apply_async(pool_read,args=(q,))

    p.close()
    p.join()
    print "end"