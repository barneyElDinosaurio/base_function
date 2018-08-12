# -*-coding=utf-8-*-
# @Time : 2018/8/7 15:41
# @File : enterprise_credit.py


import re

import requests
import time
from lxml import etree
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.support.ui import WebDriverWait
# from webapi import settings
# from barcode.proxy import get_proxy
import codecs

DRIVER_PATH = r'D:\Download\chromedriver_win32\chromedriver.exe'


def strip_func(ret):
    pattern = re.compile('\s+', re.S)
    for k in ret:
        if ret[k]:
            ret[k] = pattern.sub('', ret[k])
    return ret


def call_func(function_name, url):
    return eval(function_name)(url)


def get_content(url, retry=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    for i in range(retry):
        try:
            # proxies = get_proxy()
            r = requests.get(url=url, headers=headers, timeout=10)
            # r = requests.get(url=url, headers=headers,proxies=proxies,timeout=10)
            if r.status_code == 200:
                return r.text

            elif i == (retry - 1):
                return '404'

        except Exception as e:
            print("Exception: {}".format(e))
            # retry = retry - 1

    return None


def splash_site(url):
    splash_url = 'http://10.18.6.102:8050/render.html'
    args = {'url': url, 'timeout': 15, 'iamge': 0, 'wait': 4
           }
    response = requests.get(splash_url, params=args)
    print(response.text)
    return response.text


# 无头浏览器获取
def fake_browser(url, wait=0.5, headless=True):
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    options.add_argument('--ignore-certificate-errors')

    if headless:
        options.add_argument('--headless')

    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=DRIVER_PATH,
                               chrome_options=options)

    browser.implicitly_wait(10)
    browser.get(url)
    # WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath('//div[@id="dom"]'))
    time.sleep(wait)
    # try:
    #     browser.switch_to_alert().dismiss()
    # except Exception as e:
    #     print(e)

    txt = browser.page_source
    # print(txt)
    # s = Selector(text=txt)
    # print(txt)
    # try:
    #     browser.close()
    # except Exception as e:
    #     print(e)
    browser.quit()
    return txt


# 广东 兄弟节点
def guangdong(url):
    ret = {}
    r = get_content(url)

    if r == '404':
        return {'status': '404'}

    if r is None:
        return {'status': 'Timeout'}

    tree = Selector(text=r)

    credit_code = tree.xpath('//span[contains(text(),"信用代码/注册号")]/following::*[1]/text()').extract_first()
    registered_code = tree.xpath('//span[contains(text(),"注册号：")]/following::*[1]/text()').extract_first()
    enterprise_name = tree.xpath('//span[contains(text(),"名称：")]/following::*[1]/text()').extract_first()
    enterprise_type = tree.xpath('//span[contains(text(),"类型：")]/following::*[1]/text()').extract_first()
    legal_person = tree.xpath('//span[contains(text(),"法定代表人")]/following::*[1]/text()').extract_first()
    operator = tree.xpath('//span[contains(text(),"经营者")]/following::*[1]/text()').extract_first()
    registered_capital = tree.xpath('//span[contains(text(),"注册资本")]/following::*[1]/text()').extract_first()
    built_date = tree.xpath('//span[contains(text(),"成立日期")]/following::*[1]/text()').extract_first()
    registered_date = tree.xpath('//span[contains(text(),"注册日期")]/following::*[1]/text()').extract_first()

    operating_from = tree.xpath(
        '//span[contains(text(),"营业期限自") or contains(text(),"经营期限自")]/following::*[1]/text()').extract_first()
    operating_to = tree.xpath(
        '//span[contains(text(),"营业期限自至") or contains(text(),"经营期限至") or contains(text(),"营业期限至")]/following::*[1]/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//span[contains(text(),"登记机关")]/following::*[1]/text()').extract_first()

    registration_status = tree.xpath('//span[contains(text(),"登记状态")]/following::*[1]/text()').extract_first()

    date_approved = tree.xpath('//span[contains(text(),"核准日期")]/following::*[1]/text()').extract_first()

    address = tree.xpath(
        '//span[contains(text(),"住所") or contains(text(),"经营场所")]/following::*[1]/text()').extract_first()

    business_scope = tree.xpath('//span[contains(text(),"经营范围")]/following::*[1]/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope
    ret = strip_func(ret)
    return ret


# 上海 i
def shanghai(url):
    ret = dict()
    r = get_content(url)

    if r == '404':
        return {'status': '404'}

    if r is None:
        return {'status': 'Timeout'}

    tree = Selector(text=r)

    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/i/text()').extract_first()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/i/text()').extract_first()
    enterprise_name = tree.xpath('//*[contains(text(),"名称：")]/i/text()').extract_first()
    enterprise_type = tree.xpath('//*[contains(text(),"类型：")]/i/text()').extract_first()
    legal_person = tree.xpath('//*[contains(text(),"法定代表人")]/i/text()').extract_first()
    operator = tree.xpath('//*[contains(text(),"经营者")]/i/text()').extract_first()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/i/text()').extract_first()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/i/text()').extract_first()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/i/text()').extract_first()

    operating_from = tree.xpath('//*[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/i/text()').extract_first()
    operating_to = tree.xpath('//*[contains(text(),"经营期限至") or contains(text(),"营业期限自至")]/i/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/i/text()').extract_first()

    # 登记状态
    registration_status = tree.xpath('//*[contains(text(),"登记状态")]/i/text()').extract_first()
    date_approved = tree.xpath('//*[contains(text(),"核准日期")]/i/text()').extract_first()

    address = tree.xpath(
        '//*[contains(text(),"住所") or contains(text(),"经营场所") or contains(text(),"营业场所")]/i/text()').extract_first()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/i/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope

    ret = strip_func(ret)

    return ret


# 江苏 p fake
def jiansu(url):
    ret = dict()
    # url = 'http://www.jsgsj.gov.cn:58888/province/infoQueryServlet.json?pt&c=75B161B67BE862B1B9B50CF1A1420D05086E9CB1272995C97DF99E81BB73B09702815BD1D1F8C048226850D691D0B23B5A5398514C27F4C5BE613C937889291D'
    r = fake_browser(url)
    if r is None:
        return None
    tree = Selector(text=r)

    credit_code = tree.xpath('//span[contains(text(),"信用代码")]/../p/text()').extract_first()
    registered_code = tree.xpath('//span[contains(text(),"注册号")]/../p/text()').extract_first()
    enterprise_name = tree.xpath('//span[contains(text(),"名称")]/../p/text()').extract_first()
    enterprise_type = tree.xpath('//span[contains(text(),"类型")]/../p/text()').extract_first()
    legal_person = tree.xpath('//span[contains(text(),"法定代表人") or contains(text(),"负责人")]/../p/text()').extract_first()
    operator = tree.xpath('//span[contains(text(),"经营者")]/../p/text()').extract_first()
    registered_capital = tree.xpath('//span[contains(text(),"注册资本")]/../p/text()').extract_first()
    built_date = tree.xpath('//span[contains(text(),"成立日期")]/../p/text()').extract_first()
    registered_date = tree.xpath('//span[contains(text(),"注册日期")]/../p/text()').extract_first()

    operating_from = tree.xpath(
        '//span[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/../p/text()').extract_first()
    operating_to = tree.xpath(
        '//span[contains(text(),"经营期限至") or contains(text(),"营业期限自至")]/../p/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//span[contains(text(),"登记机关")]/../p/text()').extract_first()

    # 登记状态
    registration_status = tree.xpath('//span[contains(text(),"登记状态")]/../p/text()').extract_first()
    date_approved = tree.xpath('//span[contains(text(),"核准日期")]/../p/text()').extract_first()

    address = tree.xpath('//span[contains(text(),"住所") or contains(text(),"经营场所")]/../p/text()').extract_first()

    business_scope = tree.xpath('//span[contains(text(),"经营范围")]/../p/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope

    ret = strip_func(ret)
    return ret


# 广州
def guangzhou(url):
    ret = dict()
    r = get_content(url)

    if r == '404':
        return {'status': '404'}

    if r is None:
        return {'status': 'Timeout'}

    tree = Selector(text=r)
    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/../td/text()').extract_first()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/../td/span/text()').extract_first()
    enterprise_name = tree.xpath('//*[contains(text(),"名称")]/../td/text()').extract_first()
    enterprise_type = tree.xpath('//*[contains(text(),"类型")]/../td/text()').extract_first()
    legal_person = tree.xpath('//*[contains(text(),"法定代表人")]/../td/text()').extract_first()
    operator = tree.xpath('//*[contains(text(),"经营者")]/../td/text()').extract_first()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/../td/text()').extract_first()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/../td/text()').extract_first()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/../td/text()').extract_first()

    operating_from = tree.xpath(
        '//*[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/../td/text()').extract_first()
    operating_to = tree.xpath('//*[contains(text(),"经营期限至") or contains(text(),"营业期限自至")]/../td/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/../td/text()').extract_first()

    # 登记状态
    registration_status = tree.xpath('//*[contains(text(),"状态")]/../td/text()').extract_first()
    date_approved = tree.xpath('//*[contains(text(),"核发日期")]/../td/text()').extract_first()

    address = tree.xpath('//*[contains(text(),"住所") or contains(text(),"经营场所")]/../td/span/text()').extract_first()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/../td[1]').xpath('string(.)').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope

    ret = strip_func(ret)

    return ret


# 珠海
def zhuhai(url):
    ret = dict()
    r = get_content(url)
    if r is None:
        return None
    home_page = Selector(text=r)
    try:
        detail_url = home_page.xpath('//form/table/tr//a/@href').extract_first()
    except Exception as e:
        print(e)

    if detail_url:
        print('detail page', detail_url)

        r_content = fake_browser(detail_url)
        tree = Selector(text=r_content)

        credit_code = tree.xpath('//div[@class="cert-num"]/text()').extract()
        registered_code = tree.xpath('//*[contains(text(),"注册号")]/following-sibling::*[1]/text()').extract()
        if len(credit_code) == 0:
            credit_code = tree.xpath('//td[contains(text(),"信用代码")]/following-sibling::*[1]/text()').extract()
            registered_code = tree.xpath('//td[contains(text(),"注册号")]/following-sibling::*[1]/text()').extract()
            enterprise_name = tree.xpath('//td[contains(text(),"名称")]/following-sibling::*[1]/text()').extract_first()
            enterprise_type = tree.xpath(
                '//td[contains(text(),"商事主体类型")]/following-sibling::*[1]/text()').extract_first()
            legal_person = tree.xpath('//td[contains(text(),"法定代表人")]/following-sibling::*[1]/text()').extract()
            operator = tree.xpath('//td[contains(text(),"信用代码")]/following-sibling::*[1]/text()').extract()
            # operator = tree.xpath('//*[contains(text(),"信用代码")]/following-sibling::*[1]/text()').extract()
            registered_capital = tree.xpath('//td[contains(text(),"注册资本")]/following-sibling::*[1]/text()').extract()
            built_date = tree.xpath('//td[contains(text(),"成立日期")]/following-sibling::*[1]/text()').extract()
            registered_date = tree.xpath('//td[contains(text(),"注册日期")]/following-sibling::*[1]/text()').extract()

            operating_from = tree.xpath('//td[contains(text(),"经营期限自")]/following-sibling::*[1]/text()').extract()
            operating_to = tree.xpath(
                '//td[contains(text(),"营业期限自至") or contains(text(),"经营期限至") or contains(text(),"营业期限至")]/following-sibling::*[1]/text()').extract()

            # 登记机关 核准日期
            registration_authority = tree.xpath(
                '//td[contains(text(),"登记机关")]/following-sibling::*[1]/text()').extract()

            # 登记状态
            registration_status = tree.xpath(
                '//td[contains(text(),"	企业状态")]/following-sibling::*[1]/text()').extract()
            date_approved = tree.xpath('//td[contains(text(),"核准日期")]/following-sibling::*[1]/text()').extract_first()

            address = tree.xpath('//td[contains(text(),"经营场所")]/following-sibling::*[1]/text()').extract()
            if not address:
                address = tree.xpath('//td[contains(text(),"经营场所")]/following-sibling::*[1]/text()').extract()

            business_scope = tree.xpath('//td[contains(text(),"经营场所")]/following-sibling::*[1]/text()').xpath(
                '//*[contains(text(),"经营场所")]/following-sibling::*[1]/text()').extract_first()

        else:
            enterprise_name = tree.xpath('//div[@class="cert-content cert-name"]/text()').extract()
            enterprise_type = tree.xpath('//div[@class="cert-content cert-type"]/text()').extract()
            legal_person = tree.xpath('//div[@class="cert-content cert-operator2"]/text()').extract()
            operator = tree.xpath('//div[@class="cert-content cert-operator"]/text()').extract()
            # operator = tree.xpath('//*[contains(text(),"cert-content cert-operator")]/following-sibling::*[1]/text()').extract()
            registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/following-sibling::*[1]/text()').extract()
            built_date = tree.xpath('//div[@class="cert-content cert-date2"]/text()').extract()
            registered_date = tree.xpath('//*[contains(text(),"注册日期")]/following-sibling::*[1]/text()').extract()

            operating_from = tree.xpath(
                '//*[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/../td/text()').extract()
            operating_to = tree.xpath(
                '//*[contains(text(),"经营期限至") or contains(text(),"营业期限自至")]/../td/text()').extract()

            # 登记机关 核准日期
            registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/following-sibling::*[1]/text()').extract()

            # 登记状态
            registration_status = tree.xpath('//*[contains(text(),"登记状态")]/following-sibling::*[1]/text()').extract()
            date_approved = tree.xpath('//*[contains(text(),"核发日期")]/following-sibling::*[1]/text()').extract_first()

            address = tree.xpath('//div[@class="cert-content cert-address2"]/text()').extract()
            if not address:
                address = tree.xpath('//div[@class="cert-content cert-address"]/text()').extract()

            business_scope = tree.xpath('//*[contains(text(),"经营范围")]/following-sibling::*[1]/text()').xpath(
                'string(.)').extract_first()

        ret['credit_code'] = ''.join(credit_code)
        try:
            ret['registered_code'] = registered_code[1]
        except Exception as e:
            ret['registered_code'] = None
        ret['enterprise_name'] = ''.join(enterprise_name)
        ret['enterprise_type'] = ''.join(enterprise_type)
        ret['registered_capital'] = ''.join(registered_capital)
        ret['built_date'] = ''.join(built_date)
        ret['registered_date'] = ''.join(registered_date)
        ret['registration_status'] = ''.join(registration_status)
        ret['legal_person'] = ''.join(legal_person)
        ret['operator'] = ''.join(operator)
        ret['operating_from'] = ''.join(operating_from)
        ret['operating_to'] = ''.join(operating_to)
        ret['registration_authority'] = registration_authority[0]
        ret['date_approved'] = date_approved
        ret['address'] = ''.join(address)
        ret['business_scope'] = business_scope

        ret = strip_func(ret)

        return ret

    else:
        ret = {'result': '没找到具体链接'}
        return ret


# 郑州
def zhengzhou(url):
    ret = dict()
    r = fake_browser(url, wait=3)
    tree = Selector(text=r)
    if r is None:
        return None
    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/../div/text()').extract_first()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/../div/text()').extract_first()
    enterprise_name = tree.xpath('//*[contains(text(),"企业名称")]/../div/text()').extract_first()
    enterprise_type = tree.xpath('//*[contains(text(),"类型")]/../div/text()').extract_first()
    legal_person = tree.xpath('//*[contains(text(),"法定代表人")]/../div/text()').extract_first()
    operator = tree.xpath('//*[contains(text(),"经营者")]/../div/text()').extract_first()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/../div/text()').extract_first()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/../div/text()').extract_first()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/../div/text()').extract_first()

    operating_from = tree.xpath(
        '//*[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/../div/text()').extract_first()
    operating_to = tree.xpath(
        '//*[contains(text(),"经营期限至") or contains(text(),"营业期限自至")]/../div/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/../div/text()').extract_first()

    # 登记状态
    registration_status = tree.xpath('//*[contains(text(),"登记状态")]/../div/text()').extract_first()
    date_approved = tree.xpath('//*[contains(text(),"核准日期")]/../div/text()').extract_first()

    address = tree.xpath('//*[contains(text(),"地址") or contains(text(),"经营场所")]/../div/text()').extract_first()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/../div/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope

    ret = strip_func(ret)

    return ret


# 江西
def jiangxi(url):
    ret = dict()
    # url = 'http://www.jsgsj.gov.cn:58888/province/infoQueryServlet.json?pt&c=75B161B67BE862B1B9B50CF1A1420D05086E9CB1272995C97DF99E81BB73B09702815BD1D1F8C048226850D691D0B23B5A5398514C27F4C5BE613C937889291D'
    r = fake_browser(url, wait=3)
    tree = Selector(text=r)
    if r == '404':
        return {'status': '404'}

    if r is None:
        return {'status': 'Timeout'}

    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/../span/text()').extract()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/../span/text()').extract()
    enterprise_name = tree.xpath('//*[contains(text(),"名称")]/../span/text()').extract()
    enterprise_type = tree.xpath('//*[contains(text(),"类型")]/../span/text()').extract()
    legal_person = tree.xpath('//*[contains(text(),"法定代表人")]/../span/text()').extract()
    operator = tree.xpath('//*[contains(text(),"经营者")]/../span/text()').extract()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/../span/text()').extract()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/../span/text()').extract()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/../span/text()').extract()

    operating_from = tree.xpath('//*[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/../span/text()').extract()
    operating_to = tree.xpath('//*[contains(text(),"经营期限至") or contains(text(),"营业期限至")]/../span/text()').extract()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/../span/text()').extract()

    # 登记状态
    registration_status = tree.xpath('//*[contains(text(),"登记状态")]/../span/text()').extract()
    date_approved = tree.xpath('//*[contains(text(),"核准日期")]/../span/text()').extract()

    address = tree.xpath('//*[contains(text(),"住所") or contains(text(),"经营场所")]/../span/text()').extract()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/../span/text()').extract()

    ret['credit_code'] = ''.join(credit_code)
    ret['registered_code'] = ''.join(registered_code)
    ret['enterprise_name'] = ''.join(enterprise_name)
    ret['enterprise_type'] = ''.join(enterprise_type)
    ret['registered_capital'] = ''.join(registered_capital)
    ret['built_date'] = ''.join(built_date)
    ret['registered_date'] = ''.join(registered_date)
    ret['registration_status'] = ''.join(registration_status)
    ret['legal_person'] = ''.join(legal_person)
    ret['operator'] = ''.join(operator)
    ret['operating_from'] = ''.join(operating_from)
    ret['operating_to'] = ''.join(operating_to)
    ret['registration_authority'] = ''.join(registration_authority)
    ret['date_approved'] = ''.join(date_approved)
    ret['address'] = ''.join(address)
    ret['business_scope'] = ''.join(business_scope)

    ret = strip_func(ret)

    return ret


# 陕西
def shanxi(url):
    ret = {}
    r = get_content(url)
    tree = Selector(text=r)
    if r == '404':
        return {'status': '404'}

    if r is None:
        return {'status': 'Timeout'}

    credit_code = tree.xpath('//*[contains(text(),"注 册 号")]/following::*[1]/text()').extract_first()
    registered_code = tree.xpath('//*[contains(text(),"注册号：")]/following::*[1]/text()').extract_first()
    enterprise_name = tree.xpath(
        '//*[contains(text(),"名称") or contains(text(),"个体字号")]/following::*[1]/text()').extract_first()
    enterprise_type = tree.xpath('//*[contains(text(),"类    型")]/following::*[1]/text()').extract_first()
    legal_person = tree.xpath('//*[contains(text(),"法定代表人")]/following::*[1]/text()').extract_first()
    operator = tree.xpath('//*[contains(text(),"经营者")]/following::*[1]/text()').extract_first()
    registered_capital = tree.xpath('//span[contains(text(),"注册资本")]/following::*[1]/text()').extract_first()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/following::*[1]/text()').extract_first()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/following::*[1]/text()').extract_first()

    operating_from = tree.xpath(
        '//*[contains(text(),"营业期限自") or contains(text(),"经营期限自")]/following::*[1]/text()').extract_first()
    operating_to = tree.xpath(
        '//*[contains(text(),"营业期限至") or contains(text(),"经营期限至")]/following::*[1]/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/following::*[1]/text()').extract_first()

    registration_status = tree.xpath('//span[contains(text(),"登记状态")]/following::*[1]/text()').extract_first()

    date_approved = tree.xpath('//span[contains(text(),"核准日期")]/following::*[1]/text()').extract_first()

    address = tree.xpath(
        '//*[contains(text(),"住    所") or contains(text(),"经营场所")]/following::*[1]/text()').extract_first()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/following::*[1]/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope
    ret = strip_func(ret)

    return ret


# 顺德 使用上海的库
# def shunde(url):

# 安徽
def anhui_second(url):
    ret = dict()
    r = fake_browser(url, wait=3)
    tree = Selector(text=r)
    if r is None:
        return None
    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/../p/text()').extract_first()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/../p/text()').extract_first()
    enterprise_name = tree.xpath('//*[contains(text(),"企业名称")]/../p/text()').extract_first()
    enterprise_type = tree.xpath('//*[contains(text(),"类型")]/../p/text()').extract_first()
    legal_person = tree.xpath('//*[contains(text(),"法定代表人")]/../p/text()').extract_first()
    operator = tree.xpath('//*[contains(text(),"经营者")]/../p/text()').extract_first()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/../p/text()').extract_first()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/../p/text()').extract_first()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/../p/text()').extract_first()

    operating_from = tree.xpath(
        '//*[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/../p/text()').extract_first()
    operating_to = tree.xpath(
        '//*[contains(text(),"经营期限至") or contains(text(),"营业期限自至")]/../p/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/../p/text()').extract_first()

    # 登记状态
    registration_status = tree.xpath('//*[contains(text(),"登记状态")]/../p/text()').extract_first()
    date_approved = tree.xpath('//*[contains(text(),"核准日期")]/../p/text()').extract_first()

    address = tree.xpath('//*[contains(text(),"地址") or contains(text(),"经营场所")]/../p/text()').extract_first()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/../p/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope

    ret = strip_func(ret)
    return ret


# 北京
def beijing(url):
    ret = dict()
    r = fake_browser(url, wait=3)
    tree = Selector(text=r)
    if r is None:
        return None
    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/following::*[1]/text()').extract_first()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/following::*[1]/text()').extract_first()
    enterprise_name = tree.xpath('//*[contains(text(),"名称")]/following::*[1]/text()').extract_first()
    enterprise_type = tree.xpath('//*[contains(text(),"类型")]/following::*[1]/text()').extract_first()
    legal_person = tree.xpath('//*[contains(text(),"法定代表人")]/following::*[1]/text()').extract_first()
    operator = tree.xpath('//*[contains(text(),"负责人")]/following::*[1]/text()').extract_first()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/following::*[1]/text()').extract_first()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/following::*[1]/text()').extract_first()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/following::*[1]/text()').extract_first()

    operating_from = tree.xpath(
        '//*[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/following::*[1]/text()').extract_first()
    operating_to = tree.xpath(
        '//*[contains(text(),"经营期限至") or contains(text(),"营业期限至")]/following::*[1]/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/following::*[1]/text()').extract_first()

    # 登记状态
    registration_status = tree.xpath('//*[contains(text(),"经营状态")]/following::*[1]/text()').extract_first()
    date_approved = tree.xpath('//*[contains(text(),"核准日期")]/following::*[1]/text()').extract_first()

    address = tree.xpath('//*[contains(text(),"地址") or contains(text(),"营业场所")]/following::*[1]/text()').extract_first()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/following::*[1]/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope

    ret = strip_func(ret)
    return ret


# 贵州
def guizhou(url):
    ret = dict()
    r = fake_browser(url, wait=3)
    tree = Selector(text=r)
    if r is None:
        return None
    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/span/text()').extract()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/span/text()').extract()
    enterprise_name = tree.xpath('//*[contains(text(),"名称")]/span/text()').extract()
    enterprise_type = tree.xpath('//*[contains(text(),"类型")]/span/text()').extract()
    legal_person = tree.xpath('//*[contains(text(),"法定代表人")]/span/text()').extract()
    operator = tree.xpath('//*[contains(text(),"经营者")]/span/text()').extract()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/span/text()').extract()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/span/text()').extract()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/span/text()').extract()

    operating_from = tree.xpath('//*[contains(text(),"经营期限自") or contains(text(),"营业期限自")]/span/text()').extract()
    operating_to = tree.xpath('//*[contains(text(),"经营期限至") or contains(text(),"营业期限至")]/span/text()').extract()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/span/text()').extract()

    # 登记状态
    registration_status = tree.xpath('//*[contains(text(),"登记状态")]/span/text()').extract()
    date_approved = tree.xpath('//*[contains(text(),"核准日期")]/span/text()').extract()

    address = tree.xpath('//*[contains(text(),"住所") or contains(text(),"经营场所")]/span/text()').extract()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/span/text()').extract()

    ret['credit_code'] = ''.join(credit_code)
    ret['registered_code'] = ''.join(registered_code)
    ret['enterprise_name'] = ''.join(enterprise_name)
    ret['enterprise_type'] = ''.join(enterprise_type)
    ret['registered_capital'] = ''.join(registered_capital)
    ret['built_date'] = ''.join(built_date)
    ret['registered_date'] = ''.join(registered_date)
    ret['registration_status'] = ''.join(registration_status)
    ret['legal_person'] = ''.join(legal_person)
    ret['operator'] = ''.join(operator)
    ret['operating_from'] = ''.join(operating_from)
    ret['operating_to'] = ''.join(operating_to)
    ret['registration_authority'] = ''.join(registration_authority)
    ret['date_approved'] = ''.join(date_approved)
    ret['address'] = ''.join(address)
    ret['business_scope'] = ''.join(business_scope)

    ret = strip_func(ret)

    return ret


# 深圳
def shenzhen(url):
    ret = {}
    r = get_content(url)
    tree = Selector(text=r)
    if r == '404':
        return {'status': '404'}

    if r is None:
        return {'status': 'Timeout'}

    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/span/span/text()').extract_first()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/span/span/text()').extract_first()
    enterprise_name = tree.xpath('//*[@id="company_title_box"]/text()').extract_first()
    enterprise_type = tree.xpath('//*[contains(text(),"类型")]/span/span/text()').extract_first()
    legal_person = tree.xpath('//*[@id="lblCompanyBoss"]/text()').extract_first()
    operator = tree.xpath('//*[contains(text(),"经营者")]/span/span/text()').extract_first()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/span/span/text()').extract_first()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/span/span/text()').extract_first()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/span/span/text()').extract_first()

    operating_from = tree.xpath(
        '//*[contains(text(),"营业期限自") or contains(text(),"经营期限自")]/span/span/text()').extract_first()
    operating_to = tree.xpath(
        '//*[contains(text(),"营业期限自至") or contains(text(),"经营期限至")]/span/span/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/span/span/text()').extract_first()

    registration_status = tree.xpath('//*[@id="lblEntStatusCode"]/text()').extract_first()

    date_approved = tree.xpath('//*[contains(text(),"核准日期")]/span/span/text()').extract_first()

    address = tree.xpath(
        '//*[contains(text(),"住所") or contains(text(),"经营场所")]/span/span/text()').extract_first()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/span/span/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope
    ret = strip_func(ret)
    return ret


# 福建
def fujian(url):
    ret = {}
    r = fake_browser(url, 5, headless=False)
    tree = Selector(text=r)
    if r is None:
        return None
    credit_code = tree.xpath('//*[contains(text(),"信用代码")]/following::*[1]/text()').extract_first()
    registered_code = tree.xpath('//*[contains(text(),"注册号")]/following::*[1]/text()').extract_first()
    enterprise_name = tree.xpath('//*[contains(text(),"主体名称")]/following::*[1]/text()').extract_first()
    enterprise_type = tree.xpath('//*[contains(text(),"类型")]/following::*[1]/text()').extract_first()
    legal_person = tree.xpath('///*[contains(text(),"法人")]/following::*[1]/text()').extract_first()
    operator = tree.xpath('//*[contains(text(),"负责人")]/following::*[1]/text()').extract_first()
    registered_capital = tree.xpath('//*[contains(text(),"注册资本")]/following::*[1]/text()').extract_first()
    built_date = tree.xpath('//*[contains(text(),"成立日期")]/following::*[1]/text()').extract_first()
    registered_date = tree.xpath('//*[contains(text(),"注册日期")]/following::*[1]/text()').extract_first()

    operating_from = tree.xpath(
        '//*[contains(text(),"营业期限自") or contains(text(),"经营期限自")]/following::*[1]/text()').extract_first()
    operating_to = tree.xpath(
        '//*[contains(text(),"营业期限自至") or contains(text(),"经营期限至")]/following::*[1]/text()').extract_first()

    # 登记机关 核准日期
    registration_authority = tree.xpath('//*[contains(text(),"登记机关")]/following::*[1]/text()').extract_first()

    registration_status = tree.xpath('//*[contains(text(),"状态")]/following::*[1]/text()').extract_first()

    date_approved = tree.xpath('//*[contains(text(),"核准日期")]/following::*[1]/text()').extract_first()

    address = tree.xpath(
        '//*[contains(text(),"住所") or contains(text(),"经营场所")]/following::*[1]/text()').extract_first()

    business_scope = tree.xpath('//*[contains(text(),"经营范围")]/following::*[1]/text()').extract_first()

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope
    ret = strip_func(ret)
    return ret


def extract_info(url):
    r = get_content(url)

    if r == '404':
        return {'status': '404'}

    if r is None:
        return {'status': 'Timeout'}

    content = html_to_text(r)

    ret, flag = find_info(content)

    if ret['credit_code'] is None and ret['registered_code'] is None:
        print('use - fake browser')
        # r = fake_browser(url, wait=3, headless=False)
        r=splash_site(url)
        content = html_to_text(r)
        ret, flag = find_info(content)

    return ret


def html_to_text(r):
    p = re.compile('<script.*?</script>', re.S)
    ret = re.sub(p, '', r)
    tree = Selector(text=ret)
    content = tree.xpath('string(.)').extract_first()
    brace_pattern = re.compile('\{.*?\}', re.S)
    p2 = re.compile('\r\n', re.S)
    content = re.sub(p2, '', content)
    content = brace_pattern.sub('', content)
    return content


def find_info(content):
    # print('纯文本')
    # content = codecs.open('html_code1.txt', 'r', encoding='utf-8').read()
    # print(content)
    credit_code_pattern = re.compile('社会信用代码.*?([A-Z0-9]+)', re.S)
    registered_code_pattern = re.compile('注册号.*?([A-Z0-9]+)', re.S)
    enterprise_name_pattern = re.compile('(单位名称|企业名称|名称：).*?([\u4e00-\u9fa5]+)', re.S)
    enterprise_type_pattern = re.compile('类型.*?([\u4e00-\u9fa5]+)', re.S)
    legal_person_pattern = re.compile('法定代表人.*?([\u4e00-\u9fa5]+)', re.S)
    registered_capital_pattern = re.compile('(注册资本|开办资金数额).*?(\d+.*?[\u4e00-\u9fa5]+)', re.S)
    built_date_pattern = re.compile('成立日期.*?(\d+.*?[\u4e00-\u9fa5\d+]+)', re.S)
    registered_date_pattern = re.compile('注册日期.*?(\d+.*?[\u4e00-\u9fa5\d+]+)', re.S)
    registration_status_pattern = re.compile('登记状态.*?([\u4e00-\u9fa5].*?)[\s]+', re.S)
    operator_pattern = re.compile('(经营者|投资人).*?([\u4e00-\u9fa5]+)', re.S)
    operating_from_pattern = re.compile('(营业|经营)期限自.*?(\d.*?)[\s]+', re.S)
    operating_to_pattern = re.compile('(营业|经营)期限至.*?(\d.*?)[\s]+', re.S)
    date_approved_pattern = re.compile('核准日期.*?(\d.*?)[\s]+', re.S)
    registration_authority_pattern = re.compile('登记机关.*?([\u4e00-\u9fa5]+)[\s]+', re.S)
    address_pattern = re.compile('(住所|场所|地址).*?([\u4e00-\u9fa5].*?)[\s]+', re.S)
    business_scope_pattern = re.compile('(业务范围|经营范围).*?([\u4e00-\u9fa5].*?)[\s]+', re.S)
    ret = {}
    # print(content)
    if credit_code_pattern.search(content):
        credit_code = credit_code_pattern.search(content).group(1)
    else:
        credit_code = None

    if registered_code_pattern.search(content):
        registered_code = registered_code_pattern.search(content).group(1)
    else:
        registered_code = None

    if enterprise_name_pattern.search(content):
        enterprise_name = enterprise_name_pattern.search(content).group(2)
    else:
        enterprise_name = None

    if enterprise_type_pattern.search(content):
        enterprise_type = enterprise_type_pattern.search(content).group(1)
    else:
        enterprise_type = None

    if legal_person_pattern.search(content):
        legal_person = legal_person_pattern.search(content).group(1)
    else:
        legal_person = None

    if registered_capital_pattern.search(content):
        registered_capital = registered_capital_pattern.search(content).group(2)
    else:
        registered_capital = None

    if built_date_pattern.search(content):
        built_date = built_date_pattern.search(content).group(1)
    else:
        built_date = None

    if registration_status_pattern.search(content):
        registration_status = registration_status_pattern.search(content).group(1)
    else:
        registration_status = None

    if operator_pattern.search(content):
        operator = operator_pattern.search(content).group(2)
    else:
        operator = None

    if operating_from_pattern.search(content):
        operating_from = operating_from_pattern.search(content).group(2)
    else:
        operating_from = None

    if registered_date_pattern.search(content):
        registered_date = registered_date_pattern.search(content).group(1)
    else:
        registered_date = None

    if operating_to_pattern.search(content):
        operating_to = operating_to_pattern.search(content).group(2)
    else:
        operating_to = None

    if date_approved_pattern.search(content):
        date_approved = date_approved_pattern.search(content).group(1)
    else:
        date_approved = None

    if registration_authority_pattern.search(content):
        registration_authority = registration_authority_pattern.search(content).group(1)
    else:
        registration_authority = None

    if address_pattern.search(content):
        address = address_pattern.search(content).group(2)
    else:
        address = None

    if business_scope_pattern.search(content):
        business_scope = business_scope_pattern.search(content).group(2)
    else:
        business_scope = None

    ret['credit_code'] = credit_code
    ret['registered_code'] = registered_code
    ret['enterprise_name'] = enterprise_name
    ret['enterprise_type'] = enterprise_type
    ret['registered_capital'] = registered_capital
    ret['built_date'] = built_date
    ret['registered_date'] = registered_date
    ret['registration_status'] = registration_status
    ret['legal_person'] = legal_person
    ret['operator'] = operator
    ret['operating_from'] = operating_from
    ret['operating_to'] = operating_to
    ret['registration_authority'] = registration_authority
    ret['date_approved'] = date_approved
    ret['address'] = address
    ret['business_scope'] = business_scope
    ret = strip_func(ret)
    # print(ret)
    return ret, True


# extract_info(url)
# find_info()
# text=get_content(url)
# print(text)
# url = 'http://www.szcredit.com.cn/web/GSZJGSPT/QyxyDetail.aspx?rid=8a8084555aef1870015af0ea8f69026f&cid=92440300MA5EEY5XXT'
# url='https://www.sgs.gov.cn/notice/query/queryEntInfoMain.do?uuid=NEK5QOkBQXrDSYfcFsUJu_LueQYWpODP'
# url='http://dzhy.haaic.gov.cn/yzt/toHandleQuery.do?id=YmVobG9xcXF2dXV0emx5ZHJm&uniScID=amJrbW9ycXheVXVxVWhcdXRy&jumpFlag=false'
# url='http://hb.gsxt.gov.cn/qyxxgsAction_initQyxyxxMain.action?nbxh=MTYwMDAwMDA0MDY2Nzk5MTY5'
url='https://www.xiamencredit.gov.cn:8084/xmgsggfw/SsztServlet?flag=sszt&action=viewSsztMobile&qyid=2c97f1904efbe266014f0096b2d21dd6&pritype=06&sfsszt=1&sfjyyc=2&qymc='
# url='http://www.jsgsj.gov.cn:58888/province/infoQueryServlet.json?pt&c=75B161B67BE862B17DBE79325695AE4DCEAF8A43CFA9D2C9215DC25E4FB0B1D69111A1C295F314DE7C94A2CF9F428B1FD10ED118C48CECD8038AF9E73108D656'
# url='http://218.22.14.66:8082/yzt/toHandleQuery.do?id=ZWFnbG9xcXh0dnZxeWdyZWxi&uniScID=amJqcG9ycnFeVXNCdFR5JnBQ&jumpFlag=false'
# url='https://www.sgs.gov.cn/notice/query/queryEntInfoMain.do?uuid=ocWbkyycild04Ej_XwtbpNz8a6VNO3xg'
# url='http://www.szcredit.com.cn/web/GSZJGSPT/QyxyDetail.aspx?rid=8a80845b5b671574015ba3f61b841849&cid=92440300MA5EGYHW9F'
# url='http://gsxt.gdgs.gov.cn//GSpublicity/GSpublicityList.html?jumpid=rO0ABXQASntzZXJ2aWNlOmVudEluZm8sZW50Tm86MzVjYWJlZjMtMDEyMi0xMDAwLWUwMDctZTkw%0D%0AOTBhMDUwMTE1LHJlZ09yZzo0NDA1MDh9%0D%0A'
# url='http://gsxt.gdgs.gov.cn//GSpublicity/GSpublicityList.html?jumpid=rO0ABXQASntzZXJ2aWNlOmVudEluZm8sZW50Tm86MGUyM2Y3ZDMtMDE0OS0xMDAwLWUwMDAtOWNk%0D%0ANjBhMGEwMTE1LHJlZ09yZzo0NDEzMDJ9%0D%0A'
# url='http://gsxt.gdgs.gov.cn//GSpublicity/GSpublicityList.html?service=entInfo&entNo=1be0c514-013f-1000-e000-48480a76b50b&regOrg=441924'
# url='http://113.98.246.4:7013/mw/c/g/jibencolumn.html?tabname=dwzxCwqPbvw=&id=mM6yRJe0HxZ003CnLejYkdRANxdahInI'
print(extract_info(url))
# splash_site(url)

# print(get_content(url,retry=5))

def reg_test():
    import codecs
    content = codecs.open('html2.txt', encoding='utf8').read()
    # enterprise_name_pattern = re.compile('(单位名称|企业名称|名称：)[^、].*?([\u4e00-\u9fa5]+)', re.S)
    # test_p=enterprise_name_pattern.search(content).group(2)
    # test_p = re.search('名称：[^、](.*?) ',content,re.S).group()
    ret = html_to_text(content)
    print(ret)

# reg_test()

# html_to_text()
