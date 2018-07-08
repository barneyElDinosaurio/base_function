import time
import random
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
server = '127.0.0.1'

m = QueueManager(address=(server,8001),authkey='hello')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()
while not task.empty():
	image_url = task.get(True,timeout=10)
	print('Download url {}'.format(image_url))
	time.sleep(random.random())
	result.put('Sucessful url {}'.format(image_url))

print('finish all the task')


