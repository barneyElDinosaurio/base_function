try:
	import cPickle as pickle
except:
	import pickle

# save to pickle
# d = dict(tilte='New world', body='This is boy')
# f = open('temp.plk','w')
# pickle.dump(d,f)


# read pickle
# f=open('temp.plk','r')
# d=pickle.load(f)
# print type(d)
# print d


'''
# create process by fork
import os

if __name__=='__main__':
	print 'current process {} start'.format(os.getpid())

	pid = os.fork()

	if pid < 0 :
		print 'error in fork'

	elif pid ==0:
		print 'i am child process {} and my parent process is {}'.format(os.getpid(),os.getppid())
	else:
		print 'i {} create a child process {}'.format(os.getpid(),pid)

'''


'''

import os
from multiprocessing import Process

def sub_proc(name):
	print 'chile process {} is running'.format(os.getpid())

def create_multiprocess():
	print 'parent process is {}'.format(os.getpid())

	for i in range(5):
		p = Process(target=sub_proc,args=(i,))
		print 'process will start'
		p.start()

		p.join()
	print 'main process end'



create_multiprocess()
'''



'''
from multiprocessing import Pool
import os
import time
import random

def run_process(name):
	print 'process no.{} and pid : {} is running'.format(name,os.getpid())
	time.sleep(random.random())
	print 'process no.{} and pid {} end'.format(name,os.getpid())


def parent_process():
	print 'parent pid is {}'.format(os.getpid())
	p =Pool()

	for i in range(10):
		p.apply_async(run_process,args=(i,))

	print 'waiting all proces is done'
	p.close()
	print 'p is close'
	p.join()
	print 'end of function'

parent_process()
'''

import multiprocessing
import random
import time
import os
def msg_send(pipe,urls):
	for url in urls:
		print 'process {} is sending {}'.format(os.getpid(),url)
		pipe.send(url)
		time.sleep(random.random())

def msg_recv(pipe):
	while True:
		print 'process {} received msg {} '.format(os.getpid(),pipe.recv())



def create_process_pipe():
	pipe = multiprocessing.Pipe()

	p1 = multiprocessing.Process(target=msg_send,args=(pipe[0],['url_'+str(i) for i in range(10)]))

	p2 = multiprocessing.Process(target=msg_recv,args=(pipe[1],))

	p1.start()
	p2.start()
	p1.join()
	p2.join()

	print 'end of function'

create_process_pipe()