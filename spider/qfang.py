# coding: utf-8
import requests
import qfang


url = 'http://m.qfang.com/beijing/garden?page=4'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Accept': '*/*',
    'Content-Length': '6',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8''',
    'Cookie': 'qchatid=8c000cb7-e46f-49a9-8ed9-5b1e365db2a9; CITY_NAME=SHENZHEN; _jzqx=1.1502184218.1502184218.1.jzqsr=shenzhen%2Eqfang%2Ecom|jzqct=/.-; _jzqy=1.1502162895.1505202967.2.jzqsr=baidu|jzqct=%E6%B7%B1%E5%9C%B3%E6%94%BE%E5%81%87.jzqsr=baidu|jzqct=%E6%88%BF%E5%A4%A9%E4%B8%8B; _jzqckmp=1; LXB_REFER=www.baidu.com; _jzqa=1.891413787490525200.1502162895.1502184218.1505202967.4; _jzqc=1; JSESSIONID=aaaayFLmRLxNDeLJoh15v; cookieId=c9d4bf28-a066-4f56-842d-a3fc1c9721e6; sid=78979f0b-a6b9-4fc8-9336-31d045991b8f; Hm_lvt_de678bd934b065f76f05705d4e7b662c=1505202967; Hm_lpvt_de678bd934b065f76f05705d4e7b662c=1505204320; _ga=GA1.3.1951310847.1505203374; _gid=GA1.3.509609154.1505203374',
    'Host': 'm.qfang.com',
    'Origin': 'http://m.qfang.com',
    'Pragma': 'no-cache',
    'Referer': 'http://m.qfang.com/beijing/garden',
    'X-Requested-With': 'XMLHttpRequest'}
p = requests.post(url=url, data={'more': 4},headers=header)
print(p.status_code)
s = p.text
print(s)
