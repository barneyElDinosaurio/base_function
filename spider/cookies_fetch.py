# -*-coding=utf-8-*-
__author__ = 'Rocky'
import requests
import os
import json
import sqlite3
# import cookielib
# import Cookie
# import urllib2
import random
import time
import redis
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import config

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
    print(resp.text)

# 使用无头浏览器登录并保存cookie
def getFromWebBrowser():

    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    driver = webdriver.Chrome(executable_path=r'D:\OneDrive\Python\selenium\chromedriver.exe',
                              chrome_options=options)
    driver.implicitly_wait(40)
    url = 'http://30daydo.com/login/'
    driver.get(url)
    username = driver.find_element_by_id("aw-login-user-name")
    username.clear()
    username.send_keys(config.username)
    psd = driver.find_element_by_id("aw-login-user-password")
    psd.clear()
    psd.send_keys(config.password)
    commit = driver.find_element_by_id("login_submit")
    commit.click()
    time.sleep(5)
    cookies = driver.get_cookies()
    cookies_dct={}
    for c in cookies:
        # print(c)
        cookies_dct[c.get('name')]=c.get('value')

    update_cookie(config.username,cookies_dct)

#使用cookie登录, 使用request

def login_with_cookie():
    cookie = json.loads(load_cookie())
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    url = 'http://30daydo.com/notifications/'
    r = requests.get(url=url,cookies=cookie,headers=headers)
    r.encoding='utf8'
    print(r.text)


# 更新cookie
def update_cookie(name,cookies):
    r = redis.StrictRedis('10.18.6.102',decode_responses=False,db=3)
    if r.get(name) is None:
        r.set(name,json.dumps(cookies))
        print("save")
    else:
        print('cookies is existed!')

# 获取cookie
def load_cookie():
    r = redis.StrictRedis('10.18.6.102',decode_responses=False,db=3)
    name = random.choice(r.keys())
    cookie = r.get(name)
    return cookie

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
        print(row)
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


class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

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

    
if __name__ == "__main__":
    # cookie='lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; _jzqckmp=1; _jzqx=1.1504062784.1504605523.6.jzqsr=sz%2Efang%2Elianjia%2Ecom|jzqct=/.jzqsr=captcha%2Elianjia%2Ecom|jzqct=/; ubtreadd_b=; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699,1504258015,1504675657; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504675949; _smt_uid=59a62d3f.3df2aef3; _jzqa=1.1378702697002941000.1504062784.1504605523.1504675658.12; _jzqc=1; _jzqb=1.2.10.1504675658.1; _gid=GA1.2.235704312.1504588604; aliyungf_tc=AQAAAJ+TD1lFgAsAnkIYdH+u777bV6KX; select_city=320500; cityCode=su; _gat_u=1; __xsptplusUT_696=1; __xsptplus696=696.13.1504675656.1504676160.12%234%7C%7C%7C%7C%7C%23%23un_6cd_LD8h6uhQem1QRQG9agH-plMJm%23; _ga=GA1.2.331020171.1503638699; ubt_load_interval_b=1504676160161; ubt_load_interval_c=1504676160161; lianjia_ssid=0fbcdf1e-da2d-4751-d570-bc3e16a230b7; ubtd=12; gr_session_id_970bc0baee7301fa=c5746a98-e86d-4236-a0d6-4a262c3cbaff; ubta=1641808036.2641861454.1503971686808.1504676160235.1504676281816.91; ubtb=1641808036.2641861454.1504676281818.2FCA7814756D779495B76F54624DD919; ubtc=1641808036.2641861454.1504676281818.2FCA7814756D779495B76F54624DD919'
    # trans = transCookie(cookie)
    # print(trans.stringToDict())
    #csdn()
    # getFromWebBrowser()
    login_with_cookie()