# -*-coding=utf-8-*-

# @Time : 2018/9/30 16:45
# @File : download_image.py

import urllib
import urllib.request
import urllib.parse
import pymongo

import os

import time


def cbk(a, b, c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


def download(url):
    filename = url.split('/')[-1]
    # url = 'http://www.yzcetc.com/yzhynewt/EpointMisTempFile/c03b5dd9-cfe6-42ef-bb41-323461cacb7e/'+urllib.parse.quote('营业.jpg')
    path = os.path.dirname(url)
    basename = os.path.basename(url)
    encode_base_name = urllib.parse.quote(basename)
    full_path = path + '/' + encode_base_name
    try:
        print(filename)
        urllib.request.urlretrieve(url, filename, cbk)
    except Exception as e:
        print(e)
        return False
    else:
        return True


def run():
    doc = pymongo.MongoClient('10.18.6.26', port=27018)['spider']['qiyi']

    for item in doc.find({}):
        if item.get('status') is None or item.get('status') == 0:

            url = item.get('img_url')
            print('urls >>>>', url)
            if download(url):
                doc.update_one({'img_url': url}, {'$set': {'status': 1}})
            else:
                doc.update_one({'img_url': url}, {'$set': {'status': 0}})


if __name__ == '__main__':

    os.chdir('qiyi')
    # 循环下载
    while 1:
        run()
        time.sleep(60*5)