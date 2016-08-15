#-*-coding=utf-*-
#i remember that i have created another one of this python file
#http://blog.csdn.net/iloveyin/article/details/21444613
__author__ = 'xda'
import requests
def request_test():
    url='https://github.com/timeline.json'
    r=requests.get(url)
    print r.text
    print r.json()

    data={"name":"Rocky"}
    url2="http://httpbin.org/post"
    s=requests.post(url2,data)
    print s.text
    print s.url
    t=requests.post(url2,params=data)
    print t.url


request_test()
