# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:58:31 2018

@author: liuxinyu
"""
import shutil
import time

import os

import pymongo

"""
接口返回
1.成功识别则返回验证码具体内容
2.识别失败: 101
3.验证码中含有干扰线: 100
"""



import base64
import requests
import threading

def img_to_b64(img_path):
    with open(img_path,'rb') as f:
        base64_data=base64.b64encode(f.read())
    return base64_data.decode('utf-8')



def post_method():
    img_path = 'shibiecuowu1537481397.png'  # 图片路径
    img_b64 = img_to_b64(img_path) #转为base64编码
    img_dict={'img':img_b64}
    res=requests.post('http://10.18.6.102:5001/Captcha_api',data=img_dict,timeout=1)
    print(res.text)



def multi_thread():
    start = time.time()
    thread_list = []

    for i in range(100):
        t = threading.Thread(target=post_method, args=())
        thread_list.append(t)
    for t in thread_list:
        t.start()
        t.join()
    time_used = time.time() - start
    print('Time used :{} ms'.format(time_used*1000))

def barcode(img_path=None):

    url = 'http://10.18.6.107:8180/rest/qrDroid'
    # img_path ='yyzz10.jpg'
    print(img_path)
    img_str = img_to_b64(img_path)
    data = {'imgStr':img_str,'sysApplyId':'99999999999'}
    # print(data)
    r = requests.post(url=url,json=data)
    try:
        ret = r.json()
    except Exception as e:
        print(e)
        return False

    if ret.get('thirdMsg') == '识别成功':
        return True
    else:
        return False

def save_barcode_content(content):
    db = pymongo.MongoClient('10.18.6.26',port=27018)
    doc = db['spider']['qrcode']
    try:
        doc.insert({'qrcode':content})
    except Exception as e:
        print(e)


def loop_image():
    count=0
    total=0
    for (dirname, dirs, filename) in os.walk('.'):
        for file in filename:
            total+=1
            if barcode(file):
                count+=1
                print(file)

                shutil.copy(file,'successed/'+file)

    print('count >>>>',count)
    print('total >>>>',total)
    print('successful rate {}'.format(count/total*100))
# multi_thread()
# post_method()
# barcode()
loop_image()