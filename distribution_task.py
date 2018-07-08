# -*-coding=utf-8-*-
import random

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import Queue
import multiprocessing
from multiprocessing.managers import BaseManager
multiprocessing.freeze_support()
class QueueMessage(BaseManager):
    pass


def main():
    task_queue=Queue.Queue()
    result_queue=Queue.Queue()

    QueueMessage.register('get_task_queue',callable=lambda: task_queue)
    QueueMessage.register('get_result_queue',callable=lambda: result_queue)


    manager=QueueMessage(('',7777),authkey=b'abcd')
    manager.start()

    task_manager=manager.get_task_queue()
    result_manager=manager.get_result_queue()

    for i in range(10):
        t=random.randint(0,100)
        print("put %d into the queue" %t)
        task_manager.put(t)


    for j in range(10):
        try:
            t=result_manager.get(timeout=20)
            print("get %d from the queue server" %t)
        except Exception as e:
            print(e)

    manager.shutdown()

if __name__=='__main__':
    main()