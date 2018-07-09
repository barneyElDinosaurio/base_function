# -*-coding=utf-8-*-


# -*-coding=utf-8-*-
import time
import requests
import json
from lxml import etree
import pymongo

db = pymongo.MongoClient('localhost')
doc = db['NEXGO']['HLJSXR']


def get_proxy(retry=5):
    proxyurl = 'http://:8081/dynamicIp/common/getDynamicIp.do'
    count = 0
    for i in range(retry):
        try:
            r = requests.get(proxyurl, timeout=5)
        except Exception as e:
            print(e)
            count += 1
            print('代理获取失败,重试' + str(count))
            time.sleep(1)

        else:
            js = r.json()
            proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
            proxies_random = {
                'http': proxyServer
            }
            print(proxies_random)
            return proxies_random


class Spider(object):

    def __init__(self):
        self.url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信被执行人名单&cardNum=&iname={}&areaName=&pn=0&rn=10&ie=utf-8&oe=utf-8&format=json&t=1531116216885&cb=jQuery110206392930510508604_1531097441777&_=1531097441798'
        self.headers = {
            # 'Accept': "*/*",
            'Host': 'sp0.baidu.com',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:39.0) Gecko/20100101 Firefox/39.0",
            'Referer':'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&rsv_pq=abc684e300038cc0&rsv_t=621cv7Va7zN8ANNhc%2B6ifjkfvuJc%2BJA6N6e9ojyfo17jI4NdBsJhbXUc81o&rqlang=cn&rsv_enter=1&rsv_sug3=11&rsv_sug1=14&rsv_sug7=101&rsv_sug2=0&inputT=2278&rsv_sug4=3044',
            # 'Cookie': 'BAIDUID=EB2D652E163FB73C74428062BD17CDD6:FG=1; BIDUPSID=EB2D652E163FB73C74428062BD17CDD6; PSTM=1529550132; H_PS_PSSID=26522_1459_21101_20930; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'
        }

        self.cookie = {"BAIDUID": "EB2D652E163FB73C74428062BD17CDD6:FG=1",
                       'BDORZ': "B490B5EBF6F3CD402E515D22BCDA1598",
                       'BIDUPSID': "EB2D652E163FB73C74428062BD17CDD6",
                       'H_PS_PSSID': "26522_1459_21101_20930",
                       'PSINO': "7",
                       'PSTM': "1529550132"
                       }

    def gets(self):
        try:
            r = requests.get(url=self.url.format('孙新伟'), headers=self.headers,cookies=self.cookie)

            tree = etree.HTML(r.text)
            return r.text, tree
        except Exception as e:
            print(e)
            return None

    def _gets(self, url):
        # r = self.session.get(url, headers=self.headers, proxies=get_proxy())
        r = self.session.get(url, headers=self.headers, proxies=get_proxy())
        return r.text

    def posts(self, page):
        post_data = {'proselect': "", 'cityselect': "", 'disselect': "", 'curPageNO': str(page)}
        r = self.session.post(self.url, headers=self.headers, data=post_data, proxies=get_proxy())
        text = r.text
        tree = etree.HTML(r.text)
        return text, tree

    def download(self):
        r = requests.get(self.url)
        filename = 'code.png'
        with open(filename, 'wb') as f:
            f.write(r.content)

    def person_post_action(self):
        login_header = {
            'Host': 'www.hljcredit.gov.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'X-Requested-With': 'XMLHttpRequest',
            # 'Connection': 'keep-alive',
        }

        url1 = 'http://www.hljcredit.gov.cn/regController.do?checkislogin'
        data1 = {'checklogin': ''}
        self.session.post(url=url1, headers=login_header, data=data1, proxies=get_proxy())
        url2 = 'http://www.hljcredit.gov.cn/flowCalculateController.do?index'
        data2 = {'cmain': 'xycx', 'flowname': 'xyhlj'}
        flow_header = {
            'Host': 'www.hljcredit.gov.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            # 'Connection': 'keep-alive',
        }
        self.session.post(url=url2, headers=flow_header, data=data2, proxies=get_proxy())

    def parse(self):
        for i in range(5):
            text, response = self.posts(i)
            nodes = response.xpath('//table[@class="list_2_tab"]/tr')
            column_name = ['case_number', 'person_name', 'sex', 'age', 'identify_number', 'enterprise_name', 'area',
                           'executed_court', 'executed_number', 'executed_unit',
                           'execution', 'execution_detail', 'executed_item', 'not_execute', 'case_date', 'release_date']

            for node in nodes[1:]:
                d = {}
                url = 'http://www.hljcredit.gov.cn/' + node.xpath('.//td[2]/a/@href')[0].strip()
                content = self._gets(url)
                tree = etree.HTML(content)
                item_list = tree.xpath('//table[@class="for_letter"]/tr')
                for index, value in enumerate(column_name):
                    d[value] = item_list[index].xpath('.//td[2]/text()')[0].strip()
                doc.insert(d)


def main():
    spider = Spider()
    spider.gets()


if __name__ == '__main__':
    main()
