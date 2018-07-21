# -*-coding=utf-8-*-
import random
import string
import requests
import threading
import time
import multiprocessing
from multiprocessing import freeze_support
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
import gevent

# api 压力测试

def ping(threadname):

    # url='http://30daydo.com'

    url = 'http://10.18.6.101:8000/sxr/?name=0576cc884d087d5ecfdce44a14922c32&idnum=4b45ba32c45e83c1df1ab890735ef16d'
    r = requests.get(url)
    threadname='i'
    print('Thread ::: {}'.format(threadname))
    print(r.json())


def multi_thread():
    start = time.time()
    thread_list = []
    for i in range(100):
        t = threading.Thread(target=ping, args=('thread{}'.format(i),))
        thread_list.append(t)
    for t in thread_list:
        t.start()
        t.join()
    time_used = time.time() - start
    print('Time used :{}'.format(time_used))

# 多进程
def multi_process():
    start = time.time()
    p = multiprocessing.Pool(processes=8)
    for i in range(100):
        p.apply_async(ping, args=('process {}'.format(str(i)),))
    p.close()
    p.join()
    time_used = time.time() - start
    print('Time used :{}'.format(time_used))

# 协程
def gevent_case():

    pool = Pool(8)
    pool.map(ping,(range(8),))

    # print(result)
    gevent_list = [gevent.spawn(ping,str(i)) for i in range(10)]
    gevent.joinall(gevent_list)

def random_string():
    x = str(int(time.time() * 1000))
    ran_str = ''.join(random.sample(string.ascii_lowercase, 17))
    orderNo = '{}{}'.format(x, ran_str)


if __name__ == '__main__':
    # multi_thread()
    gevent_case()
    # freeze_support()
    # multi_process()
    # for _ in range(100000):
    #     z=random_string()
    #     # print(len(z))
