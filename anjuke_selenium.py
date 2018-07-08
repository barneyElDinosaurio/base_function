# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pymongo
def anjuke():
    client=pymongo.MongoClient('127.0.0.1',27017)
    db=client['test']
    collection=db['anjuke_selenium']
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=r'C:\software\chrome\chromedriver.exe',
                               chrome_options=options)
    browser.implicitly_wait(30)
    for i in range(1,101):
        browser = webdriver.Chrome(executable_path=r'C:\software\chrome\chromedriver.exe',
                                   chrome_options=options)
        browser.get('https://shenzhen.anjuke.com/community/p%d/' %i)
        l = browser.find_elements_by_xpath('//div[@_soj="xqlb"]')
        print(len(l))
        for i in l:
            item = dict()
            item['name']=i.find_element_by_xpath('.//div[@class="li-info"]/h3/a').text
            item['url']=i.find_element_by_xpath('.//div[@class="li-info"]/h3/a').get_attribute('href')
            item['location']=i.find_element_by_xpath('.//div[@class="li-info"]/address').text
            item['building_date']=i.find_element_by_xpath('.//div[@class="li-info"]/p').text
            item['price']= i.find_element_by_xpath('.//div[@class="li-side"]/p/strong').text
            #print(item)
            collection.insert(item)
        browser.close()

anjuke()