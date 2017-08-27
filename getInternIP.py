# -*-coding=utf-8-*-
import re
import urllib2
import Queue
import time
import threading
q=Queue.Queue()
def getIP():
    url='http://members.3322.org/dyndns/getip'
    req=urllib2.Request(url)
    resp=urllib2.urlopen(req).read()
    return resp

t_count=10000
count=0
start=time.time()
def divide_task(start,end,q):
    count=0
    for i in xrange(start,end):
        ip=getIP()
        #print ip
        if re.search('\.',ip) is not None:
            count=count+1
    q.put(count)
def start_run():
    task_number=200
    each_count=t_count/task_number
    thrd=[]
    for i in range(task_number):
        t=threading.Thread(target=divide_task,args=(i,i+each_count,q,))
        thrd.append(t)

    for t in thrd:
        t.start()

    for t1 in thrd:
        t1.join()
    sum=0
    while not q.empty():
        sum=sum+q.get()

    print sum


end=time.time()
'''
start_run()

if t_count==count:
    print "100%%work"

print 'time used: ',end-start
'''

print getIP()