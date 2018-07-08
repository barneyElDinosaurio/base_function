# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''

from multiprocessing import Process, Queue, Pool
import multiprocessing
import os, time, random

multiprocessing.freeze_support()
'''
# 写数据进程执行的代码:
def write(q,lock):
    lock.acquire() #加上锁
    for value in ['A', 'B', 'C','D','E','F','G','H','I','J','K']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
    lock.release() #释放锁

# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    q = manager.Queue()
    lock = manager.Lock() #初始化一把锁
    p = Pool()
    pw = p.apply_async(write,args=(q,lock))
    pr = p.apply_async(read,args=(q,))
    p.close()
    p.join()

    print
    print('所有数据都写入并且读完')
'''

'''
#运行的时候全是错误。 error
l = multiprocessing.Lock()

def job(num):
  l.acquire()
  print(num)
  l.release()
  time.sleep(1)

pool = multiprocessing.Pool(4)

lst = range(40)
for i in lst:
  pool.apply_async(job, [i])

pool.close()
pool.join()

'''

'''
from multiprocessing import Pool, Lock
import urllib2
from time import clock
from functools import partial
from multiprocessing import Manager


def send_request( data,lock):
    api_url = 'http://api.xxxx.com/?data=%s'
    start_time = clock()
    print(urllib2.urlopen(api_url % data).read())
    end_time = clock()
    lock.acquire()
    with open('request.log', 'a+') as logs:
        logs.write('request %s cost: %s\n' % (data, end_time - start_time))
    lock.release()


if __name__ == '__main__':
    data_list = ['data1', 'data2', 'data3']

    manager = Manager()

    pool = Pool(8)
    # lock = Lock()
    lock = manager.Lock()
    partial_send_request = partial(send_request, lock=lock)
    pool.map(partial_send_request, data_list)
    pool.close()
    pool.join()
'''

from multiprocessing import Pool, Lock
import urllib2
from time import clock
from functools import partial
from multiprocessing import Manager
def send_request(data):
    api_url = 'http://api.xxxx.com/?data=%s'
    start_time = time.clock()
    print(urllib2.urlopen(api_url % data).read())
    end_time = time.clock()
    lock.acquire()
    with open('request.log', 'a+') as logs:
        logs.write('request %s cost: %s\n' % (data, end_time - start_time))


    lock.release()


def init(l):
    global lock
    lock = l


if __name__ == '__main__':
    data_list = ['data1', 'data2', 'data3']
    lock = Lock()
    pool = Pool(8, initializer=init, initargs=(lock,))
    pool.map(send_request, data_list)
    pool.close()
    pool.join()