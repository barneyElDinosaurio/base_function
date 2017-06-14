# -*-coding=utf-8-*-
__author__ = 'Rocky'
import requests


def csdn():
    session = requests.session()
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'}
    url = 'http://msg.csdn.net/'
    header[
        'Cookie'] = 'uuid_tt_dd=-5697318013068753627_20160111; _ga=GA1.2.795042232.1452766190; _message_m=quvq2wle24wa4aweppwic204; UserName=yagamil; UserInfo=zMhiNgesgIlEBQ3TOqLCtx4nUI360IIq3ciBzg4EKH%2FW8mSpTANpu5cTlRFLj2Tqh%2FZzQr2rNqDtT1SZz%2Be2%2FpDkGoQxDK3IVUZXvwZ%2FEP1I4UTg6MoZkH7LDO3sjrJJ; UserNick=%E9%87%8D%E5%A4%8D%E7%9A%84%E7%94%9F%E6%B4%BB; AU=0F1; UD=%E8%AE%B0%E5%BD%95%E8%87%AA%E5%AD%A6%E7%9A%84%E5%8E%86%E7%A8%8B+%E5%88%83%E8%8D%89+www.rcdisk.com; UN=yagamil; UE="chen_jinwei@126.com"; BT=1490707396344; access-token=c2e12bff-5b27-4a91-953b-448ff6f6beac; _csdn_notify_admin_session=VE41a0d3TitrVGY2bGtXY09pZENwR1lHenhUU1NVaWc1b04wL1I3dCtDQVdadWpjMXBzdGRJL0RZR04wYldvZDBhTU96b2oycVVKeVI1UEVyUHFKbG1yNnB2b2pHRWVnWG1uc2JMM2R3YWthakRyTXZNaEpVU1NtUy9zQUJrNjd3R2lpbG5PK0paMnlyc1dyK0lTZUtRPT0tLXlPQUE1QzF5UmhDNjEvSFdtRFlQS2c9PQ%3D%3D--4569c5a32916dcf969a8b7e007c37abeb90be4f3; dc_tos=onj1dg; dc_session_id=1490707393375; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1490024083,1490024559,1490374375,1490707368; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1490707638'
    header['Cache-Control'] = 'max-age=0'
    header['Host'] = 'msg.csdn.net'
    header['Referer'] = 'http://blog.csdn.net/yagamil'
    resp = requests.get(url, headers=header)
    # resp=session.get(url,headers=header)
    print resp.text


def getFromWebBrowser():
    #not work
    import requests
    import browsercookie
    cj = browsercookie.chrome()
    r = requests.get('http://stackoverflow.com', cookies=cj)

#csdn()
#getFromWebBrowser()

import os
import sqlite3
import cookielib
import Cookie
import urllib2

def build_opener_with_chrome_cookies(domain=None):
    #同样失败了
    cookie_file_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\Cookies')
    if not os.path.exists(cookie_file_path):
        raise Exception('Cookies file not exist!')
    conn = sqlite3.connect(cookie_file_path)
    sql = 'select host_key, name, value, path from cookies'
    if domain:
        sql += ' where host_key like "%{}%"'.format(domain)

    cookiejar = cookielib.CookieJar()    # No cookies stored yet

    for row in conn.execute(sql):
        print row
        cookie_item = cookielib.Cookie(
            version=0, name=row[1], value=row[2],
                     port=None, port_specified=None,
                     domain=row[0], domain_specified=None, domain_initial_dot=None,
                     path=row[3], path_specified=None,
                     secure=None,
                     expires=None,
                     discard=None,
                     comment=None,
                     comment_url=None,
                     rest=None,
                     rfc2109=False,
            )
        cookiejar.set_cookie(cookie_item)    # Apply each cookie_item to cookiejar
    conn.close()
    return urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))    # Return opener

#build_opener_with_chrome_cookies()


