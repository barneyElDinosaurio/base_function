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
import logging

logger = logging.getLogger()

# api 压力测试

def ping(threadname):

    # name='f1f9c4b219ca6b87ca21bc696acf37ba'
    # idnum='6ff02be5ac5232c013f4e8f5dc5e9ca3'
    # orderNo='123456789123456789123456789000'
    # url = 'http://10.18.6.101:8000/sxr/?name={0}&idnum={1}&orderNo={2}'.format(name,idnum,orderNo)

    # r = requests.get(url)
    # print(r.json())

    data={'orderNo':'1234555','content':'http://www.szcredit.com.cn/web/GSZJGSPT/QyxyDetail.aspx?rid=ff86d6dce2ee483bb2b2f852cc2cb1b1&cid=9144030079921798XW'}
    r=requests.post(url='http://127.0.0.1:8002/barcode',data=data)
    print(r.json())
    threadname = 'i'
    print('Thread ::: {}'.format(threadname))
    # print(r.json())


def multi_thread():
    start = time.time()
    thread_list = []

    for i in range(100):
        t = threading.Thread(target=sxr, args=())
        thread_list.append(t)
    for t in thread_list:
        t.start()
        t.join()
    time_used = time.time() - start
    print('Time used :{} ms'.format(time_used*1000))


# 多进程
def multi_process():
    start = time.time()
    p = multiprocessing.Pool(processes=8)
    for i in range(4):
        p.apply_async(ping, args=('process {}'.format(str(i)),))
    p.close()
    p.join()
    time_used = time.time() - start
    print('Time used :{0}'.format(time_used*1000))


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

def sxr():
    # host='127.0.0.1'
    host='10.18.4.211'
    # url='http://{}:8000/sxr/?name=334c911e750c27347887de00016b5e26&idnum=50ba516c1038f17d52c6d506ab9bf745&orderNo=12345678'.format(local)
    url='http://{}:8556/sxr'.format(host)
    # 'f1f9c4b219ca6b87ca21bc696acf37ba&idnum=6ff02be5ac5232c013f4e8f5dc5e9ca3'
    # data={'name':'334c911e750c27347887de00016b5e26','orderNo':'123456789','idnum':'50ba516c1038f17d52c6d506ab9bf745'}
    # data={'name':'f1f9c4b219ca6b87ca21bc696acf37ba','idnum':'6ff02be5ac5232c013f4e8f5dc5e9ca3','orderNo':'123456789'}
    # data={'name':'路露','idnum':'320106198210040436','orderNo':'123456789'}
    data={'name':'04bd28789cb1425e0af388b7223f4537','idnum':'c62cd3435439508238fe592c427a8320','orderNo':'qqqqqqqqqqqqqqqqqq'}
    # data={'name':'冷景佳','idnum':'360423********101X','orderNo':'123456789'}
    # for _ in range(10):
    # start=time.time()
    # r=requests.get(url)
    r=requests.post(url,data=data)
    # print(r.json())
    # print('Time used:{0}\n'.format(time.time()-start))
    return True

def loop_back():
    while True:

        # local = '127.0.0.1'
        local='10.18.4.211'

        # url='http://{}:8000/sxr/?name=334c911e750c27347887de00016b5e26&idnum=50ba516c1038f17d52c6d506ab9bf745&orderNo=12345678'.format(local)
        url = 'http://{}:8556/sxr'.format(local)
        # 'f1f9c4b219ca6b87ca21bc696acf37ba&idnum=6ff02be5ac5232c013f4e8f5dc5e9ca3'
        # data={'name':'334c911e750c27347887de00016b5e26','orderNo':'123456789','idnum':'50ba516c1038f17d52c6d506ab9bf745'}
        # data={'name':'f1f9c4b219ca6b87ca21bc696acf37ba','idnum':'6ff02be5ac5232c013f4e8f5dc5e9ca3','orderNo':'123456789'}
        # data={'name':'路露','idnum':'320106198210040436','orderNo':'123456789'}
        data = {'name': '04bd28789cb1425e0af388b7223f4537', 'idnum': 'c62cd3435439508238fe592c427a8320', 'orderNo': '12345678900000'}
        # data={'name':'冷景佳','idnum':'360423********101X','orderNo':'123456789'}
        # for _ in range(10):
        # start=time.time()
        # r=requests.get(url)
        r = requests.post(url, data=data)
        print(r.json())
        # print('Time used:{0}\n'.format(time.time()-start))
        # return True
        time.sleep(3000)

def get_content(url, retry=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    for i in range(retry):

        try:
            proxies = get_proxy()
            logger.info('Proxy {}'.format(proxies))
            r = requests.get(url=url, headers=headers, timeout=10)
            # r = requests.get(url=url, headers=headers, proxies=proxies, timeout=10)
            logger.info('访问URL：{} 的状态码为{}'.format(url, r.status_code))

            if r.status_code == 200:
                return r.text

            else:
                logger.info('访问URL:: {} 状态码出错。返回非法页面或者页面不存在。'.format(url))
                # return '404'
            logger.info('retry:{} times'.format(i))
        except Exception as e:

            logger.error("访问企业:: URL {}。异常信息：{}。".format(url, e))

    return '404'

def get_proxy( retry=50):

    proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxyip)
    for i in range(1, retry + 1):
        try:
            r = requests.get(proxyurl, timeout=10)
        except Exception as e:
            logger.error('获取代理错误：{}'.format(e))
            logger.error('Failed to get proxy ip, retry {}'.format(i))
            time.sleep(1)

        else:
            js = r.json()
            proxyServer = {'http':'http://{0}:{1}'.format(js.get('ip'), js.get('port'))}
            return proxyServer

def barcode_speed():
    url='http://gsxt.gdgs.gov.cn//GSpublicity/GSpublicityList.html?service=entInfo&entNo=a9d314a0-0159-1000-e000-18c60a0c0115&regOrg=441923'
    avg_time = []
    for i in range(10):
        start=time.time()
        r=get_content(url)
        time_used = time.time()-start
        avg_time.append(time_used)
    s=0
    for i in avg_time:
        s=s+i
    print('avg time used : {}'.format(s))

def barcode_pressure():
    local='http://127.0.0.1:8002/barcode'
    data={'orderNo':'119','content':'http://gsxt.gdgs.gov.cn//GSpublicity/GSpublicityList.html?service=entInfo&entNo=a9d314a0-0159-1000-e000-18c60a0c0115&regOrg=441923'}


    avg_time =[]
    for i in range(10):
        start=time.time()
        r = requests.post(url=local, data=data)
        time_used = time.time()-start
        avg_time.append(time_used)
    s=0
    for i in avg_time:
        s=s+i
    print('total: {}'.format(s))
    print('avg time used : {} ms'.format(s/10*1000))


def proxy_speed():
    avg_time =[]
    for i in range(100):
        start=time.time()
        proxy = get_proxy()
        time_used = time.time()-start
        avg_time.append(time_used)
    s=0
    for i in avg_time:
        s=s+i
    print('total: {}'.format(s))
    print('avg time used : {} ms'.format(s/100*1000))

if __name__ == '__main__':
    # demo()
    multi_thread()

    # barcode_pressure()
    # proxy_speed()
    # gevent_case()
    # freeze_support()
    # multi_process()
    # for _ in range(100000):
    #     z=random_string()
    #     # print(len(z))
    # ping('dfd')
    # for i in range(5):
        # start=time.time()
        # sxr()
        # print("time used {} ms".format((time.time()-start)*1000))
        # multi_thread()
    # time.sleep()
    # print('Done')
    # loop_back()