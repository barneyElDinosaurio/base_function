# -*-coding=utf-8-*-
import random

import requests
import time


def _postdata():
    url = 'https://www.lagou.com/gongsi/searchPosition.json'

    # 最小header
    headers = {'Origin': 'https://www.lagou.com', 'Content-Length': '87', 'Accept-Language': 'zh,en;q=0.8,en-US;q=0.6',
               'Accept-Encoding': 'gzip, deflate, br', 'X-Anit-Forge-Code': '33435644',
               'X-Requested-With': 'XMLHttpRequest', 'X-Anit-Forge-Token': '5b95a0d3-eed5-49e9-a5e7-f02be38a2716',
               'Host': 'www.lagou.com', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
               'Connection': 'keep-alive',

               'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'Referer': 'https://www.lagou.com/gongsi/j917.html',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    data = {'companyId': '917',
            'positionFirstType': u'全部',
            'schoolJob': 'False',
            'pageNo': '1',
            'pageSize': '10'}

    for i in range(1, 10):
        data['pageNo'] = str(i)
        r = requests.post(url=url, data=data, headers=headers)
        print(r.status_code)
        js = r.json()
        # totalCount = js.get('content').get('data').get('page').get('totalCount')
        try:
            # print(r.text)
            results = js.get('content').get('data').get('page').get('result')
            print(results)
            # time.sleep(random.random()*10)
        except:
            print("can't find result")
            print(i)
            continue


def _company():
    data = {'first': 'false',
            'pn': '444',
            'sortField': '0',
            'havemark': '0'}

    headers = {'Origin': 'https://www.lagou.com', 'Content-Length': '39',
               'Accept-Language': 'zh,en;q=0.8,en-US;q=0.6', 'Accept-Encoding': 'gzip, deflate, br',
               'X-Anit-Forge-Code': '0', 'X-Requested-With': 'XMLHttpRequest', 'X-Anit-Forge-Token': 'None',
               'Host': 'www.lagou.com', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
               'Connection': 'keep-alive',
               'Cookie': 'user_trace_token=20171008235700-51c89e1e-ac41-01e7-822c-525400f775ce; LGUID=20171008235700-51c8a17f-ac41-11e7-822c-525400f775ce; JSESSIONID=ABAAABAACDBABJB2B423D18B13E1DA9574E04C3A67D18CB; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_company; LGSID=20171022205613-622e2f35-b728-11e7-a438-525400f775ce; LGRID=20171022205618-65283f3a-b728-11e7-9601-5254005c3644; _putrc=DFAF58A586D854B0; login=true; unick=%E9%99%88%E9%94%A6%E4%BC%9F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=138; index_location_city=%E6%B7%B1%E5%9C%B3; _gid=GA1.2.1723890745.1508676965; _ga=GA1.2.891768125.1507478204; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508000182,1508164186,1508336224,1508676965; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508676974',
               'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'Referer': 'https://www.lagou.com/gongsi/',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    r = requests.post(url='https://www.lagou.com/gongsi/215-0-0.json',
                      data=data,
                      headers=headers)
    print(r.status_code)
    print(r.text)


#_postdata()
_company()
