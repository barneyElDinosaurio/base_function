# coding: utf-8
import requests


def check_cookie():
    session = requests.Session()

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    url='https://m.anjuke.com/cityList/'
    r1 = session.get(url=url, headers=headers)
    print(r1.status_code)
    print(type(r1.cookies))
    # cookie里面的字段是字典
    print('cookies >>>>', r1.cookies.get_dict())
    print('sessid>>>>>>>', r1.cookies.get('sessid'))



    # for i in r1.cookies:
    #     print(i.get('sessid'))
    # print(r1.cookies['lps'])

    return_s1 = session.get(url=url, headers=headers)
    print(return_s1.status_code)
    print('cookies >>>>', return_s1.cookies.get_dict())
    print('sessid>>>>>>>', return_s1.cookies.get('sessid'))

    # for i in return_s1.cookies:
    #     print(i)
    print(session.cookies.get_dict())

check_cookie()
