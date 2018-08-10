# -*-coding=utf-8-*-
import random
import string
import requests
import threading
import time
import multiprocessing
from multiprocessing import freeze_support
from gevent import monkey
# monkey.patch_all()
from gevent.pool import Pool
import gevent


# api 压力测试

def ping(threadname):

    import requests

    name='f1f9c4b219ca6b87ca21bc696acf37ba'
    idnum='6ff02be5ac5232c013f4e8f5dc5e9ca3'
    orderNo='123456789123456789123456789000'
    url = 'http://10.18.6.101:8000/sxr/?name={0}&idnum={1}&orderNo={2}'.format(name,idnum,orderNo)

    r = requests.get(url)
    print(r.json())


    threadname = 'i'
    print('Thread ::: {}'.format(threadname))
    # print(r.json())


def multi_thread():
    start = time.time()
    thread_list = []
    for i in range(1000):
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
    for i in range(4):
        p.apply_async(ping, args=('process {}'.format(str(i)),))
    p.close()
    p.join()
    time_used = time.time() - start
    print('Time used :{}'.format(time_used))


# 协程
def gevent_case():
    pool = Pool(8)
    pool.map(ping, (range(8),))

    # print(result)
    gevent_list = [gevent.spawn(ping, str(i)) for i in range(10)]
    gevent.joinall(gevent_list)


def random_string():
    x = str(int(time.time() * 1000))
    ran_str = ''.join(random.sample(string.ascii_lowercase, 17))
    orderNo = '{}{}'.format(x, ran_str)


def demo():
    '''
    url: 请求地址url
    data: 字典,key为url,该值为请求的企业信用url
    '''

    url = 'http://10.18.6.101:8000/barcode'
    data = {
        'url': 'http://gsxt.gdgs.gov.cn//GSpublicity/GSpublicityList.html?jumpid=rO0ABXQASntzZXJ2aWNlOmVudEluZm8sZW50Tm86N2Q3ZjljMTAtMDE0OC0xMDAwLWUwMDEtMzA2%0D%0AMTBhMGEwMTE1LHJlZ09yZzo0NDEzMDJ9%0D%0A'}
    r = requests.post(url, data)
    print(r.json())


if __name__ == '__main__':
    # demo()
    # multi_thread()
    # gevent_case()
    # freeze_support()
    # multi_process()
    # for _ in range(100000):
    #     z=random_string()
    #     # print(len(z))
    ping('dfd')