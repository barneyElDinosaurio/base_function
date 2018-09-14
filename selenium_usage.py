# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def template():
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    driver = webdriver.Chrome(executable_path=r'D:\OneDrive\Python\selenium\chromedriver.exe',
                              chrome_options=options)
    driver.implicitly_wait(40)


def login_demo():
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    driver = webdriver.Chrome(executable_path=r'D:\OneDrive\Python\selenium\chromedriver.exe',
                              chrome_options=options)
    driver.implicitly_wait(40)
    url=''
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
    cookies=driver.get_cookies()

    for c in cookies:
        print(c)
    driver.close()
    driver.quit()


def anjuke():
    # browser = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=r'C:\software\chrome\chromedriver.exe',
                               chrome_options=options)
    browser.implicitly_wait(60)
    # browser.get("https://www.crunchbase.com/app/search/companies/")
    for i in range(1, 2):
        browser.get('https://shenzhen.anjuke.com/community/p%d/' % i)
        try:
            browser.findElement(By.id('web_200'))
        except:
            print("Error")
        cookiess = browser.get_cookies()
        print('cookies:', cookiess)
        print(type(cookiess))
        print(len(cookiess))
        for i in cookiess:
            for k, v in i.items():
                print(k, v)
        # cookie=browser.get_cookie('new_session')
        # print('cookie',cookie)
        # print(type(cookie))
        l = browser.find_elements_by_xpath('//div[@_soj="xqlb"]')
        print(len(l))
        for i in l:
            '''
            print('Name:',i.find_element_by_xpath('.//div[@class="li-info"]/h3/a').text)
            print('Link:',i.find_element_by_xpath('.//div[@class="li-info"]/h3/a').get_attribute('href'))
            print('Address',i.find_element_by_xpath('.//div[@class="li-info"]/address').text)
            print('Built date:',i.find_element_by_xpath('.//div[@class="li-info"]/p').text)
            print('Price: ' , i.find_element_by_xpath('.//div[@class="li-side"]/p/strong').text)
            '''
        # print(browser.current_url)
        # print(browser.title)

        browser.close()
    # time.sleep(60)


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
        count = count+1
    raw_input('enter')


def example():
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    # options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=r'D:\Download\chromedriver_win32\chromedriver.exe',
                               chrome_options=options)

    browser.implicitly_wait(60)
    # url='http://members.3322.org/dyndns/getip'
    url = 'http://www.hljcredit.gov.cn/WebCreditQueryService.do?gssearch&type=sxbzxr&detail=true&sxbzxrmc=&proselect=&cityselect=&disselect=&curPageNO=1'
    browser.get(url)
    # time.sleep(1)
    # WebDriverWait(browser,5).until(lambda x: x.find_element_by_xpath('//div[@id="dom"]'))
    time.sleep(12)

    txt = browser.page_source

    print(txt)
    ret = browser.find_element_by_xpath('//table[@class="list_2_tab"]/tbody/tr[2]//a[1]')
    ret.click()
    time.sleep(20)
    print(ret)
    # time.sleep(12)

    # browser.send_keys(Keys.DOWN)
# netease()
# anjuke()

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

# anjuke()
# key_operation()
# shop()
# example()
login_demo()