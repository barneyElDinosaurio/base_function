# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''

import requests
from lxml import etree

session = requests.Session()
from scrapy.selector import Selector

get_crsl = 'https://passport.zujuan.com/login'
first_header = {'Host': 'passport.zujuan.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip,deflate,br', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8'}

s = session.get(get_crsl, headers=first_header)
# print(s.text)
tree = Selector(text=s.text)
csrf = tree.xpath('//input[@name="_csrf"]/@value').extract_first()

login_url = 'https://passport.zujuan.com/login?jump_url=https%3A%2F%2Fm.zujuan.com'

login_header = {'Host': 'passport.zujuan.com', 'Connection': 'keep-alive', 'Content-Length': '165', 'Accept': '*/*',
                'Origin': 'https://passport.zujuan.com', 'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'Referer': 'https://passport.zujuan.com/login', 'Accept-Encoding': 'gzip,deflate,br',
                'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
                # 'Cookie': 'device=310bdaba05b30bb632f66fde9bf3e2b91ebc4d607c250c2e1a1d9e0dfb900f01a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22device%22%3Bi%3A1%3BN%3B%7D;jump_url=7efb7d600a0688ce502e8ae92f2a80fd7c19f7672a19ecaaf51eda1f6ebdd3efa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22jump_url%22%3Bi%3A1%3Bs%3A20%3A%22https%3A%2F%2Fm.zujuan.com%22%3B%7D;_csrf=4437c0ec2d6f8226561cacdf9055c595dab37d0dd05af26ce79021f362b19133a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22c0ttNa_bWlgdOPbBHJRCh8bxqe4mGZ0g%22%3B%7D;Hm_lvt_6de0a5b2c05e49d1c850edca0c13051f=1535617512;_ga=GA1.2.1479394878.1535617779;_gid=GA1.2.870226030.1535617779;_gat_gtag_UA_112991577_1=1;_sync_login_identity=36fd383060e034288f52c98c2a63b70d53b051f65eab9da587ec0e0ebbb79c30a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22_sync_login_identity%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D;PHPSESSID=9jg86eo35akac78v1i3fu1lsn5;Hm_lpvt_6de0a5b2c05e49d1c850edca0c13051f=1535618821'
                }
data = {
    '_csrf': csrf,
    'LoginForm[username]': '13653978879',
    'LoginForm[password]': '123456'
}

log_ret = session.post(url=login_url,
                       headers=login_header,
                       data=data)
print(log_ret.text)

