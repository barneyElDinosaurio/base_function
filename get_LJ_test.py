# -*-coding=utf-8-*-
import requests
city_list={"zh": 733, "san": 108, "xm": 2170, "xa": 3850, "gz": 9304, "cd": 10157, "cs": 2773, "cq": 6237, "zs": 382, "nj": 4786, "ty": 95, "tj": 5315, "ls": 22, "wn": 26, "hz": 4526, "dl": 2498, "fs": 1522, "wc": 35, "dg": 1040, "hui": 647, "bj": 10825, "wh": 4826, "hk": 144, "jn": 3531, "hf": 2632, "yt": 1336, "wx": 945, "sjz": 2149, "sz": 4834, "sy": 2161, "km": 1348, "qd": 3698, "qh": 55}
headers= {
            'Host': 'soa.dooioo.com',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'User-Agent': 'UCWEB/2.0 (Linux; U; Adr 2.3; zh-CN; MI-ONEPlus) U2/1.0.0 UCBrowser/8.6.0.199 U2/1.0.0 Mobile',
            'X-Requested-With': 'XMLHttpRequest'
            #'Proxy-Authorization': self.authHeader
        }
city_link=['sz','gz','sh']
for i in city_list.keys():
    url='http://soa.dooioo.com/api/v4/online/house/xiaoqu/search?access_token=7poanTTBCymmgE0FOn1oKp&channel=xiaoqu&cityCode=%s&client=wap&limit_count=20&limit_offset=0' %i
    r=requests.get(url,headers=headers)
    print r.json()['data']['total_count']