# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Email: weigesysu@qq.com
'''
import requests
import json
from lxml import etree


def getContent():
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname=%E8%AF%B8%E8%91%9B&areaName=&pn=13&rn=10&ie=utf-8&oe=utf-8&format=json&t=1529662298628&cb=jQuery1102016673961426878225_1529662064306&_=1529662064378'

    # url1 = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信被执行人&cardNum=&iname=陈&areaName=&pn=0'
    # url2='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信被执行人&cardNum=&iname=b'\xe6\x97\xb6'&areaName=&pn=0'
    headers = {
        'Accept': '*/*', 'Accept-Encoding': 'gzip,deflate,br', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
        'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
        'Cookie': 'BAIDUID=C459F789B96EDC64D968698B40CF0EB2:FG=1;BIDUPSID=C459F789B96EDC64D968698B40CF0EB2;PSTM=1529375614;H_PS_PSSID=1435_21098_18560_26430_20929;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;PSINO=3',
        'Host': 'sp0.baidu.com', 'Pragma': 'no-cache',
        'Referer': 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA&oq=%25E5%25A4%25B1%25E4%25BF%25A1%25E8%25A2%25AB%25E6%2589%25A7%25E8%25A1%258C%25E4%25BA%25BA&rsv_pq=d971ea7000015588&rsv_t=b50dWdhvxoeP9syF9bJkhqWClc8wUiQNJpmr6zi5ayWjxqtGbrsGtHa2N28&rqlang=cn&rsv_enter=0&prefixsug=%25E5%25A4%25B1%25E4%25BF%25A1%25E8%25A2%25AB%25E6%2589%25A7%25E8%25A1%258C%25E4%25BA%25BA&rsp=0',
        'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.87Safari/537.36'
        }

    r = requests.get(url, headers=headers)
    # js= json.loads(r.text)
    print(r.text)
    tree = etree.HTML(r.text)
    return r.text, tree


def getContentPost():
    url = 'http://113.108.219.40/Dop/Search/SafetyAccidentList.aspx'

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
               'Cache-Control': 'no-cache', 'Content-Length': '15813',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': 'ASP.NET_SessionId=d0h5taqngsoemhvyuevuteqq;UM_distinctid=1641b08da9a800-0e1bb87bdc335a-601a147a-1fa400-1641b08da9b2b9;CNZZDATA1261062804=671075873-1529461922-%7C1529480518',
               'Host': '113.108.219.40', 'Origin': 'http://113.108.219.40', 'Pragma': 'no-cache',
               'Proxy-Connection': 'keep-alive', 'Referer': 'http://113.108.219.40/Dop/Search/SafetyAccidentList.aspx',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.87Safari/537.36'}

    data = {
        '__VIEWSTATE': '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',
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$AspNetPager1',
        '__EVENTARGUMENT': 2,
        'ctl00$ContentPlaceHolder1$txtPRJName': '',
        'ctl00$ContentPlaceHolder1$txtCheckCode': '',
        # 'ctl00$ContentPlaceHolder1$hidCheckCodeMark': 233.75339642602944
    }

    r = requests.post(url, headers=headers, data=data)
    print(r.text)
    text = r.text
    tree = etree.HTML(r.text)
    return text, tree


def download():
    url = 'http://113.108.219.40/Dop/CheckCode.aspx'
    r = requests.get(url)
    filename = 'code.png'
    with open(filename, 'wb') as f:
        f.write(r.content)


def main():
    getContent()
    # getContentPost()
    # download()


if __name__ == '__main__':
    main()
