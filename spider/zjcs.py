# -*-coding=utf-8-*-

# @Time : 2018/9/12 16:52
# @File : zjcs.py
import json

import time
from selenium import webdriver
import requests


def request_demo():
    headers = {'Accept': 'application/json,text/javascript,*/*;q=0.01',
               'Accept-Encoding': 'gzip,deflate',
               'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
               'Cache-Control': 'no-cache',
               'Connection': 'keep-alive',
               # 'Content-Length': '172',
               'Content-Type': 'application/json',
               'Cookie': 'ICITYSession=3914ef9b861a46bdbca65fd29ba01d93;selectedRegion=420000000000;selectedRegionName=%E6%B9%96%E5%8C%97%E7%9C%81;selectedRegionParentId=0;selectedRegionId=AA6D43EB827C4965B1F9238623CD57D1',
               'Host': 'www.hbzjfw.gov.cn',
               'Origin': 'http://www.hbzjfw.gov.cn',
               'Pragma': 'no-cache',
               'Referer': 'http://www.hbzjfw.gov.cn/imng/icity/browse/agency_institution',
               'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'
               }

    p = 1
    url = 'http://www.hbzjfw.gov.cn/imng/api-v2/hubei.app.icity.browse.agencyinfo.AgencyinfoCmd/agencyQuery?s=aa96831536892029911&t=6705_c73651_1536894400000'
    page_detail = {"agencyname": "", "business_range": "", "sDropDown": None, "register_org": "", "orgtype": "",
                   "qualitydegree": "", "colocation": "", "star_level": "", "workaddr": "", "start": 20, "limit": 10}

    r = requests.post(url=url, headers=headers, json=page_detail)
    # print(r.json())
    print(r.text)


def selenium_demo():
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    driver = webdriver.Chrome(executable_path=r'D:\OneDrive\Python\selenium\chromedriver.exe',
                              chrome_options=options)
    driver.implicitly_wait(40)
    url = 'http://www.hbzjfw.gov.cn/imng/icity/browse/agency_institution'
    driver.get(url)
    time.sleep(10)
    print(driver.page_source)


request_demo()
# selenium_demo()
