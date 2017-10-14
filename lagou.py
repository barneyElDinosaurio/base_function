# -*-coding=utf-8-*-
import random

import requests
import time


def _postdata():
    url = 'https://www.lagou.com/gongsi/searchPosition.json'

    # 最小header
    headers = {'Origin': 'https://www.lagou.com', 'Content-Length': '87', 'Accept-Language': 'zh,en;q=0.8,en-US;q=0.6', 'Accept-Encoding': 'gzip, deflate, br', 'X-Anit-Forge-Code': '33435644', 'X-Requested-With': 'XMLHttpRequest', 'X-Anit-Forge-Token': '5b95a0d3-eed5-49e9-a5e7-f02be38a2716', 'Host': 'www.lagou.com', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36', 'Connection': 'keep-alive', 'Cookie': 'user_trace_token=20160612223035-3a02d006-30aa-11e6-a343-5254005c3644; LGUID=20160612223035-3a02d566-30aa-11e6-a343-5254005c3644; JSESSIONID=ABAAABAACDBAAIAF33B4C87F595BE43FE5DBD6846EA46FE; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _putrc=DFAF58A586D854B0; login=true; unick=%E9%99%88%E9%94%A6%E4%BC%9F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=124; TG-TRACK-CODE=index_search; SEARCH_ID=78ff057aeb2b4837979c6966e1840c32; index_location_city=%E6%B7%B1%E5%9C%B3; _gid=GA1.2.1335763621.1507978370; _ga=GA1.2.499625224.1465741835; LGSID=20171014185251-d2e2289c-b0cd-11e7-9550-5254005c3644; LGRID=20171014185300-d8c73858-b0cd-11e7-94ed-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507809365,1507978370; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507978380', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'Referer': 'https://www.lagou.com/gongsi/j917.html', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}


    data = {'companyId': '917',
            'positionFirstType': u'全部',
            'schoolJob': 'False',
            'pageNo': '1',
            'pageSize': '10'}

    for i in range(1,10):
        data['pageNo']=str(i)
        r = requests.post(url=url, data=data, headers=headers)
        print r.status_code
        js = r.json()
        #totalCount = js.get('content').get('data').get('page').get('totalCount')
        try:
            print r.text
            results = js.get('content').get('data').get('page').get('result')
            #time.sleep(random.random()*10)
        except:
            print "can't find result"
            print i
            continue
    #print totalCount
    #for i in results:
    '''
    i=7
    data['pageNo']=str(i)
    r = requests.post(url=url, data=data, headers=headers)
    print r.status_code
    js = r.json()
    print r.text
    #totalCount = js.get('content').get('data').get('page').get('totalCount')
    try:
        results = js.get('content').get('data').get('page').get('result')
    except:
        print "can't find result"
        #print i
        #continue
    '''


_postdata()
