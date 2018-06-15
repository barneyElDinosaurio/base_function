import random
import time
import os
from multiprocessing.managers import BaseManager
import Queue

task_queue = Queue.Queue()
result_queue = Queue.Queue()

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

manager =QueueManager(address=('',8001),authkey='hello')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for url in ['Image_url'+str(i) for i in range(10)]:
	print 'put url {} to task'.format(url)
	task.put(url)

print 'try to get result'

for i in range(10):
	print 'result is {}'.format(result.get(timeout=10))

manager.shutdown()