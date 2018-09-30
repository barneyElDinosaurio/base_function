# -*-coding=utf-8-*-

# @Time : 2018/9/30 16:45
# @File : download_image.py

import urllib
import urllib.request
import urllib.parse
import pymongo

import os


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
    filename = url.split('/')[-2] + '.jpg'
    # url = 'http://www.yzcetc.com/yzhynewt/EpointMisTempFile/c03b5dd9-cfe6-42ef-bb41-323461cacb7e/'+urllib.parse.quote('营业.jpg')
    path = os.path.dirname(url)
    basename = os.path.basename(url)
    encode_base_name = urllib.parse.quote(basename)
    full_path = path + '/' + encode_base_name
    try:
        print(full_path)
        urllib.request.urlretrieve(full_path, filename, cbk)
    except Exception as e:
        print(e)
        return False
    else:
        return True


def run():
    doc = pymongo.MongoClient('10.18.6.26', port=27018)['spider']['yyzz_photo']

    for item in doc.find({}):
        if item.get('status') is None or item.get('status') == 0:

            url = item.get('image_urls')
            print('urls >>>>', url)
            if download(url):
                doc.update_one({'image_urls': url}, {'$set': {'statue': 1}})
            else:
                doc.update_one({'image_urls': url}, {'$set': {'statue': 0}})


if __name__ == '__main__':
    run()
