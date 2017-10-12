# -*-coding=utf-8-*-
import requests


def _postdata():
    url = 'https://www.lagou.com/gongsi/searchPosition.json'

    # 最小header
    headers = {
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
               'Referer': 'https://www.lagou.com/gongsi/j917.html',
               }

    data = {'companyId': 917,
            'positionFirstType': u'全部',
            'schoolJob': False,
            'pageNo': 1,
            'pageSize': 10}
    r = requests.post(url=url, data=data, headers=headers)
    print r.status_code
    js = r.json()
    totalCount = js.get('content').get('data').get('page').get('totalCount')
    results = js.get('content').get('data').get('page').get('result')
    print totalCount
    for i in results:




_postdata()
