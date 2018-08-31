# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import requests

session = requests.Session()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,br', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
    'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
    'Host': 'www.jisilu.cn', 'Pragma': 'no-cache', 'Referer': 'https://www.jisilu.cn/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'}

s1 = session.get(url='https://www.jisilu.cn/login/', headers=headers)

url = 'https://www.jisilu.cn/account/ajax/login_process/'
data = {
    'return_url': 'https://www.jisilu.cn/',
    'user_name': '一言不发',
    'password': '123456qA',
    'net_auto_login': '1',
    '_post_type': 'ajax',
}

headers1 = {'Host': 'www.jisilu.cn', 'Connection': 'keep-alive', 'Pragma': 'no-cache',
            'Cache-Control': 'no-cache', 'Accept': 'application/json,text/javascript,*/*;q=0.01',
            'Origin': 'https://www.jisilu.cn', 'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Referer': 'https://www.jisilu.cn/login/',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8'
            }

s2 = session.post(url=url, data=data, headers=headers1)
access_header = {'Accept': '*/*', 'Accept-Encoding': 'gzip,deflate,br', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
                 'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
                 # 'Cookie': 'kbz_newcookie=1;kbzw_r_uname=%E4%B8%80%E8%A8%80%E4%B8%8D%E5%8F%91;Hm_lvt_164fe01b1433a19b507595a43bf58262=1534596284,1534815723,1535250562,1535534424;kbzw__Session=m56m8cspqr166jreqq9tpmgfg3;kbzw__user_login=7Obd08_P1ebax9aXWxr2SR_3VzDuVfAFmrCW6c3q1e3Q6dvR1YzUwtqprJ2sodiV3JinqKiomqHCp7DYzN3NqcbYk6nbpZmcndbd3dPGpJ6wlauXq5iupbaxv9Gkwtjz1ePO15CspaOYicfK4t3k4OyMxbaWl6Worpi4v7iqrZ6Jutznztu43Nm-4dWflqewo5yvjJ-tvrXEw5-YzdnM2Zm8ztzX5ouWpN_p4uXGn5erp6WXrJ-wmKSasJfG2cfR092oqpywmqqY;Hm_lpvt_164fe01b1433a19b507595a43bf58262=1535646338',
                 'Host': 'www.jisilu.cn', 'Pragma': 'no-cache', 'Referer': 'https://www.jisilu.cn/home/mine/',
                 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
                 'X-Requested-With': 'XMLHttpRequest'}

s3=session.get(url='https://www.jisilu.cn/home/ajax/index_actions/page-0__filter-', headers=access_header)
print(s3.text)