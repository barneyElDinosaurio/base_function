# -*-coding=utf-8-*-

# @Time : 2018/9/4 17:28
# @File : session_test.py

import requests

# cookies.clear
headers = {
    "method": "POST",
    "scheme": "https",
    "version": "HTTP/1.1",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "dnt": "1",
    "faces-request": "partial/ajax",
    "origin": "https://www.baidu.com",
    "referer": "https://www.baidu.com",
}

conn = requests.session()#设置一个回话
resp = conn.post('https://www.baidu.com/s?wd=findspace',headers=headers)
# 打印请求的头
print(resp.request.headers)
print(resp.cookies)
print('*'*10)
# 打印结果如下，requests已经自动填充了部分数据
# 再访问一次：
resp = conn.get('https://www.baidu.com/s?wd=findspace',headers=headers)
print(resp.request.headers)
print(resp.cookies)
