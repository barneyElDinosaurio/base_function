import requests
import json
import time

def post_function():
    headers = {
        'User-Agent': 'Microsoft IE',
        # 'Content-Type':'application/json; charset=UTF-8',
    }

    url = 'http://httpbin.org/post'
    post_data = {'username': 'Rocky', 'password': '12345678'}
    r = requests.post(url, headers=headers,	json=post_data)
    js = json.dumps(r.json(), indent=2, ensure_ascii=False)
    print(js)


def duoduojinbao():
    session = requests.Session()
    url = 'http://jinbao.pinduoduo.com/network/api/common/goodsList'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'jinbao.pinduoduo.com',
        'Origin': 'http://jinbao.pinduoduo.com',
        'Referer': 'http://jinbao.pinduoduo.com/promotion/single-promotion',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    # s=session.get('http://jinbao.pinduoduo.com',headers=headers)
    # print(s.text)

    headers2 = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'jinbao.pinduoduo.com',
        'Origin': 'http://jinbao.pinduoduo.com',
        'Referer': 'http://jinbao.pinduoduo.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',


    }
    post_data = {"keyword": "", "pageNumber": 1,
                 "pageSize": 60, "sortType": 0, "withCoupon": 0}
    print(json.dumps(post_data))
    # r = requests.post(url, headers=headers, json=post_data)
    r = requests.post(url, headers=headers, data=json.dumps(post_data))
    # print(json.dumps(r.json(), indent=2))
    # print(r.json().get('errorMsg'))
    print(r.text)


def duoduojinbao_method2():

    url = "http://jinbao.pinduoduo.com/network/api/common/goodsList"
    data = {"pageSize": 60, "pageNumber": 1, "withCoupon": 0, "sortType": 0}
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'jinbao.pinduoduo.com',
        'Origin': 'http://jinbao.pinduoduo.com',
        'Referer': 'http://jinbao.pinduoduo.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',


    }
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    # r = requests.post(url=url,data =data,headers=headers)
    print(r.text)


def cookie_read():
    url = 'http://www.hljcredit.gov.cn/WebCreditQueryService.do?gongchecklists'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Host': 'www.hljcredit.gov.cn',
        'Upgrade-Insecure-Requests':'1',
        # 'Cookie':'JSESSIONID=55GdciQL5cO4O1tHPeY3b34UbljdNY97NVNRmPmAybOQ8K4PQ74I!321925893',
        'Referer': 'http://www.hljcredit.gov.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get(url, headers=headers)
    for c in r.cookies.keys():
        print(r.cookies.get(c))

    # print(r.text)


def main():
    # post_function()
    # duoduojinbao()
    # duoduojinbao_method2()
    for _ in range(10):
    	cookie_read()
    	time.sleep(5)
if __name__ == '__main__':
    main()
