# coding: utf-8
import random
import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pymongo
import logging
import config

logger = logging.getLogger()

def getproxy():
    proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxyip)
    count = 0
    print(proxyurl)
    while count < 1000:
        try:
            ipreq = requests.get(proxyurl, timeout=10)
            # ipcontent = ipreq.content
            # print(ipcontent)
            # ipcontent = json.loads(ipcontent)

        except Exception as e:
            print(e)
            count += 1
            print('代理获取失败,重试' + str(count))
            time.sleep(1)
        else:
            ipcontent = ipreq.json()
            hip = ipcontent['ip']
            hport = ipcontent['port']
            hproxy = str(hip) + ':' + str(hport)
            return hproxy


# 代理
def template():
    proxy = getproxy()
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 999999.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

    proxy_arg = '--proxy-server=http://' + proxy
    options.add_argument(proxy_arg)
    print(proxy)
    driver = webdriver.Chrome(executable_path=r'D:\OneDrive\Python\selenium\chromedriver.exe',
                              chrome_options=options)

    driver.implicitly_wait(10)

    return driver


# 一个登陆的示例
def login_demo():
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    driver = webdriver.Chrome(executable_path=r'D:\OneDrive\Python\selenium\chromedriver.exe',
                              chrome_options=options)
    driver.implicitly_wait(40)
    url = ''
    driver.get(url)
    username = driver.find_element_by_id("aw-login-user-name")
    username.clear()
    username.send_keys('')
    psd = driver.find_element_by_id("aw-login-user-password")
    psd.clear()
    psd.send_keys('')
    commit = driver.find_element_by_id("login_submit")
    commit.click()
    time.sleep(5)
    cookies = driver.get_cookies()

    for c in cookies:
        print(c)
    driver.close()
    driver.quit()


def key_operation():
    # 滚动操作
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    browser = webdriver.Chrome(executable_path=r'C:\software\chrome\chromedriver.exe',
                               chrome_options=options)  #
    browser.implicitly_wait(60)

    browser.get('https://m.fang.com/fangjia/sz_list_pinggu/')
    # browser.send_keys(Keys.DOWN)
    count = 0
    while count < 190:
        browser.find_element_by_xpath(
            "//body[@class='whitebg']").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        count = count + 1
    input('enter')


# 使用书 selenium自动化测试 --基于python语言的书
def hlj_book():
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=r'D:\Download\chromedriver_win32\chromedriver.exe',
                               chrome_options=options)

    browser.implicitly_wait(10)
    url = 'http://www.hljcredit.gov.cn/WebCreditQueryService.do?gssearch&type=sxbzxr&detail=true&sxbzxrmc=&proselect=&cityselect=&disselect=&curPageNO=1'
    browser.get(url)
    time.sleep(random.random())
    logger.info(browser.current_url)


def anjuke():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['test']
    collection = db['anjuke_selenium']
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=r'C:\software\chrome\chromedriver.exe',
                               chrome_options=options)
    browser.implicitly_wait(30)
    for i in range(1, 101):
        browser = webdriver.Chrome(executable_path=r'C:\software\chrome\chromedriver.exe',
                                   chrome_options=options)
        browser.get('https://shenzhen.anjuke.com/community/p%d/' % i)
        l = browser.find_elements_by_xpath('//div[@_soj="xqlb"]')
        print(len(l))
        for i in l:
            item = dict()
            item['name'] = i.find_element_by_xpath('.//div[@class="li-info"]/h3/a').text
            item['url'] = i.find_element_by_xpath('.//div[@class="li-info"]/h3/a').get_attribute('href')
            item['location'] = i.find_element_by_xpath('.//div[@class="li-info"]/address').text
            item['building_date'] = i.find_element_by_xpath('.//div[@class="li-info"]/p').text
            item['price'] = i.find_element_by_xpath('.//div[@class="li-side"]/p/strong').text
            # print(item)
            collection.insert(item)
        browser.close()


def visit_ip_header():
    url = 'http://httpbin.org/headers'
    driver = template()
    driver.get(url)
    time.sleep(10)


# anjuke()
# key_operation()
# shop()
# example()
# hlj_book()
# login_demo()
visit_ip_header()
