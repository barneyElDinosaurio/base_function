# -*-coding=utf-8-*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import time

# chrome配置
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(executable_path=r'C:\Users\chenjinwei\source\chromedriver.exe',chrome_options=chrome_options)
wait = WebDriverWait(browser, 10) #等待加载最长时间
base_url = "http://ls.duowan.com"

# 爬取页数配置
start_page = int(input("输入抓取起始页："))  # input输入默认为str
end_page = int(input("输入抓取结束页："))

def parse_page():
    print('正在分析数据')
    html = browser.page_source
    doc = pq(html)
    items = doc('li.card_ch.fl').items()
    for item in items:
        ceshi = {}
        ceshi['卡组名'] = item.find('.name').attr('title')
        ceshi['职业'] = item.find('.mess > ul:nth-child(2) > li:nth-child(1)').text()
        ceshi['所需尘'] = item.find('.mess > ul:nth-child(2) > li:nth-child(3)').text()
        ceshi['类型'] = item.find('.mess > ul:nth-child(2) > li:nth-child(2)').text()
        yield ceshi
        print(ceshi)

def get_page(page):
    """
    获得page页的数据
    :param page: 需要获得数据的页数
    :return:
    """
    if page == 1:
        url = base_url + '/d/' + '.html'
    else:
        url = base_url + '/d/' + 'pag' + str(page) + '.html'
    print('正在获得' + str(page) + '页的数据')
    try:
        browser.get(url)
        print(browser.page_source)
        if page > 1:
            next_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.control')))
            # 获取下一页的button传给next_page
            next_page.click()  # 点击提交button
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'li.num'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.card_list.cs-clear')))
        print('获取数据完成')
        parse_page()
    except TimeoutException:
        get_page(page)

def main():
    """
    遍历需要爬取的page
    """
    for page in range(start_page, end_page + 1):
        get_page(page)
        time.sleep(5)

if __name__ == '__main__':
    main()