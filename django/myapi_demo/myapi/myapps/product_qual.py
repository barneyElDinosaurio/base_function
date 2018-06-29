import re
import urllib
import requests
from lxml import etree


def crawl(enterprise, page=1):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
               'Cache-Control': 'no-cache',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': 'JSESSIONID=1E6C145F5ECED886DB2908D9B0ECEA94',
               'Host': '106.37.221.138', 'Origin': 'http://106.37.221.138',
               'Pragma': 'no-cache', 'Proxy-Connection': 'keep-alive',
               'Referer': 'http://106.37.221.138/jdccgs/search?page={}'.format(page),
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'
               }

    url = 'http://106.37.221.138/jdccgs/search?page={}&pageSize=10'.format(page)
    data = {'pageSize': '10',
            'r_COMPANY_NAME': urllib.parse.quote(enterprise),
            'r_PRODUCT_NAME': '',
            'r_PRODUCT_ID': '',
            'r_HEIGHT': '280',
            'r_SPOT_CHECK_TIME': '',
            'r_ADDRESS': '',
            'r_SPOT_CHECK_RESULT': ''
            }
    try:
        r = requests.post(url, headers=headers, data=data)
        if r.status_code == 200:
            return r
    except Exception as e:
        print(e)
        return None


def parse(r):
    # num = int(re.findall('共\s+(\d+)\s+页',r.text)[0])
    # print('num page {}'.format(num))
    # if num==1:
    response = etree.HTML(r.text)
    try:
        num = int(response.xpath('//input[@id="page_pageNum"]/@value')[0])
    except:
        num = 0

    ret = []
    for i in response.xpath('//table[@id="scroll_bar"]//tr'):
        item = []
        for j in range(15):
            item.append((i.xpath('.//td')[j].xpath('.//text()')[0].strip()))
        # print(len(item))
        ret.append(item)

    return ret,num


def run(name):
    # name = '格力'
    r = crawl(name)
    ret ,num = parse(r)
    if num >1:
        for i in range(2,num+1):
            r = crawl(name,i)
            l_ret,l_num = parse(r)
            ret.extend(l_ret)
    # return parse(crawl(name))
    print(len(ret))
    print(ret)
    return ret

# run('')
