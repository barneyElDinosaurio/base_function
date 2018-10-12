# -*-coding=utf-8-*-

# @Time : 2018/9/28 10:54
# @File : fetch_qrcode.py
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:58:31 2018

@author: liuxinyu
"""
import shutil
import time
import os
import logging
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

import logging

logger = logging.getLogger()  # 不加名称设置root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
# 使用FileHandler输出到文件
fh = logging.FileHandler('log.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
# 使用StreamHandler输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
# 添加两个Handler
logger.addHandler(ch)
logger.addHandler(fh)


def img_to_b64(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data.decode('utf-8')


def post_method():
    img_path = 'shibiecuowu1537481397.png'  # 图片路径
    img_b64 = img_to_b64(img_path)  # 转为base64编码
    img_dict = {'img': img_b64}
    res = requests.post('http://10.18.6.102:5001/Captcha_api', data=img_dict, timeout=1)
    logger.info(res.text)


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
    logger.info('Time used :{} ms'.format(time_used * 1000))


def save_barcode_content(content):
    db = pymongo.MongoClient('10.18.6.26', port=27018)
    doc = db['spider']['qrcode1012']
    try:
        doc.insert({'qrcode': content})
    except Exception as e:
        logger.info(e)


def barcode(img_path=None):
    url = 'http://10.18.6.107:8180/rest/qrDroid'
    logger.info(img_path)
    img_str = img_to_b64(img_path)
    data = {'imgStr': img_str, 'sysApplyId': '99999999999'}
    r = requests.post(url=url, json=data)
    try:
        ret = r.json()
        logger.info(ret)
    except Exception as e:
        logger.info(e)
        return False

    if ret.get('thirdMsg') == '识别成功':
        save_barcode_content(ret.get('result'))
        return True
    else:
        return False


def loop_image():
    count = 0
    total = 0
    for file in os.listdir('.'):
        if os.path.isfile(file):
            total += 1
            if image_enchange(file):
                count += 1
                logger.info(file)

                shutil.move(file, 'successed/' + file)
            else:
                # os.remove(file)
                shutil.move(file,'failed/'+file)

    logger.info('count >>>>{}'.format(count))
    logger.info('total >>>>{}'.format(total))
    logger.info('successful rate {}'.format(count / total * 100))


def image_enchange(img_path):
    # img_path = '3.jpg'
    img = img_to_b64(img_path)
    data = {'imgBase64': img}
    try:
        r = requests.post(url='http://10.18.6.102:5002/qr_api', data=data)
    except Exception as e:
        logger.info(e)
        return False

    # print(r.json())
    try:
        print('content >>>>', r.text)
        ret = r.json()
        logger.info(ret)
    except Exception as e:
        logger.info(e)
        return False

    if ret.get('result'):
        save_barcode_content(ret.get('result'))
        return True
    else:
        return False


loop_image()
# image_enchange('file')
logger.info('>>>>完成')
