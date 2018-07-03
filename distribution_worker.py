#-*-coding=utf-8-*-
from multiprocessing.managers import BaseManager
import Queue

import time


def process_fun(x):
    return x*x

class QueueMessage(BaseManager):
    pass


QueueMessage.register('get_task_queue')
QueueMessage.register('get_result_queue')

seraddr='192.168.2.117'
m=QueueMessage(address=(seraddr,7777),authkey=b'abcd')
m.connect()
task=m.get_task_queue()
result=m.get_result_queue()
for i in range(10):
    try:
        time.sleep(2)
        t=task.get()
        print 'get data %s from server' %t
        s=process_fun(t)
        result.put(s)
    except Exception as e:
        print e

