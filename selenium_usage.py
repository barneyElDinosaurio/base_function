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
    driver = webdriver.Chrome(executable_path=r'C:\OneDrive\Python\selenium\chromedriver.exe',
                              chrome_options=options)
    driver.implicitly_wait(40)


def netease():
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    driver = webdriver.Chrome(executable_path=r'C:\software\chrome\chromedriver.exe',
                              chrome_options=options)
    driver.implicitly_wait(40)
    driver.get("http://30daydo.com/")
    elem_user = driver.find_element_by_tag_name("登录")
    elem_user.click()
    ''''
    elem_pwd = driver.find_element_by_name("password")
    elem_pwd.send_keys("123456")
    elem_pwd.send_keys(Keys.RETURN)
    '''
    time.sleep(5)
    assert "baidu" in driver.title
    driver.close()
    driver.quit()


def anjuke():
    # browser = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    # options.add_argument('--user-agent=Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
    # options.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
    # options.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    browser = webdriver.Chrome(executable_path=r'C:\software\chrome\chromedriver.exe',
                               chrome_options=options)
    browser.implicitly_wait(60)
    # browser.get("https://www.crunchbase.com/app/search/companies/")
    for i in range(1,2):
        browser.get('https://shenzhen.anjuke.com/community/p%d/' %i)
        try:
            browser.findElement(By.id('web_200'))
        except:
            print("Error")
        cookiess=browser.get_cookies()
        print('cookies:',cookiess)
        print(type(cookiess))
        print(len(cookiess))
        for i in cookiess:
            for k,v in i.items():
                print(k,v)
        #cookie=browser.get_cookie('new_session')
        #print('cookie',cookie)
        #print(type(cookie))
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
        #print(browser.current_url)
        #print(browser.title)

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
    #browser.send_keys(Keys.DOWN)
    count=0
    while count<190:

        browser.find_element_by_xpath("//body[@class='whitebg']").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        count=count+1
    raw_input('enter')

def shop():
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=r'D:\OneDrive\Python\selenium\chromedriver.exe',
                               chrome_options=options)

    browser.implicitly_wait(60)
    url='http://dzhy.haaic.gov.cn/yzt/toHandleQuery.do?id=YmVobG9xcXFxcnptcWh0ZHFj&uniScID=amNrbW9ycXBeVXVwRWp5fHJN&jumpFlag=false'
    browser.get(url)
    # time.sleep(1)
    WebDriverWait(browser,5).until(lambda x: x.find_element_by_xpath('//div[@id="dom"]'))
    txt=browser.page_source
    print(txt)
    #browser.send_keys(Keys.DOWN)

#netease()
#anjuke()

#key_operation()
shop()