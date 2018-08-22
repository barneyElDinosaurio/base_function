# -*-coding=utf-8-*-
import pandas as pd
# pd.set_option('display.max_rows', None) # 显示所有的列
pd.set_option('expand_frame_repr',False) # 显示行不换行
import requests
import re
import redis
r=redis.StrictRedis('10.18.6.101',decode_responses=True)
def url_re():
    txt='http://www.sgs.gov.cn/notice/query/queryEntInfoMain.do?uuid=zfvJFezgAjh3lQSoYnq4M_AkEqZHAcBK'
    ret = re.search('(http://.*)|(https://.*)', txt, re.S)
    if ret:
        print(ret.group())

def get_url(x):
    try:
        link = re.search('(http://.*)|(https://.*)', x, re.S)
        if link:
            ret= link.group()
        else:
            ret = None
        # print(x)
    except Exception as e:
        print(x)
        print(e)
        # print(x)
        ret = None

    return ret

# push url to redis
# df = pd.read_excel('qrcode_result.xlsx')
# df['url'] = df['qr_res'].map(get_url)
#
# for i in df['url']:
#     if i:
#         url=i.split(' ')[0]
#         r.lpush('barcode_url',url)


def check_ret(url):
    print('Fetching:::: {}'.format(url))
    data = {'url': url}
    p = requests.post('http://127.0.0.1:8000/barcode', data)
    try:
        js=p.json()
    # if js['']
        print(js)
    except Exception as e:
        print(e)

while 1:
    url = r.lpop('barcode_url')
    check_ret(url)
    if not url:
        break