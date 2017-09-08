# coding: utf-8
import requests
def check_cookie():
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    r1=requests.get(url='https://m.anjuke.com/cityList/',headers=headers)
    print r1.status_code
    print type(r1.cookies)
    for i in r1.cookies:
        print i
    #print r1.cookies['lps']

    s1=requests.Session()
    return_s1=s1.get(url='https://m.anjuke.com/cityList/',headers=headers)
    print return_s1.status_code
    for i in return_s1.cookies:
        print i
check_cookie()
