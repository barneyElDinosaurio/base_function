# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:55:02 2017

@author: liuxinyu
"""

# import threading
import time
import requests
# import urllib.request
from lxml import etree
import simplejson
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
# import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import re
# from datetime import datetime
import pymysql
# from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


header={
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   'Accept-Encoding':'gzip, deflate, sdch',
   'Accept-Language':'zh-CN,zh;q=0.8',
   'Cache-Control':'max-age=0',
   'Connection':'keep-alive',
   'Host':'www.hljcredit.gov.cn',
   'Upgrade-Insecure-Requests':'1',
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}


def get_web_driver(name, proxy=0):
    # print('web_driver')
    if name.lower() == 'chrome_headless_with_proxy':
        # 爬取国家公示系统网站,一定要使用代理, 不然会封IP
        path_to_chromedriver = 'chromedriver.exe'
        #            chrome_exe="c:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
        proxy_arg = '--proxy-server=' + proxy
        chrome_options.add_argument(proxy_arg)
        browser = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options)
        browser.implicitly_wait(60)
        return browser

    elif name.lower() == 'chrome_with_proxy':
        path_to_chromedriver = 'chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        proxy_arg = '--proxy-server=http://' + proxy
        chrome_options.add_argument(proxy_arg)
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

        br = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options)
        br.set_page_load_timeout(10)
        br.implicitly_wait(60)

        return br
    elif name.lower() == 'phantomjs':
        #        proxy_config=webdriver.Proxy()
        #        proxy_config.proxy_type=ProxyType.MANUAL
        #        proxy_config.http_proxy=proxy
        #        proxy_config.proxy_type=ProxyType.DIRECT
        #        proxy_config.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0")
        #        dcap["browserName"] = ("chrome")
        # dcap["http_proxy"]=(proxy)
        br = webdriver.PhantomJS(
            executable_path=r"D:\webdrive\phantomjs-2.5.0-beta2-windows\phantomjs-2.5.0-beta2-windows\bin",
            desired_capabilities=dcap)
        br.set_page_load_timeout(15)
        return br
    elif name.lower() == "chrome_noproxy":
        path_to_chromedriver = 'chromedriver.exe'
        chrome_options = webdriver.ChromeOptions()
        # proxy_arg = '--proxy-server=http://' + proxy
        # chrome_options.add_argument(proxy_arg)
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

        br = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options)
        br.set_page_load_timeout(10)
        br.implicitly_wait(60)
        return br
    elif name.lower() == "chrome_headless":

        # chrome浏览器无头模式在WINDOW下需要CHROME版本>59.0 and chromedriver 版本>2.3.0
        path_to_chromedriver = 'chromedriver.exe'
        #            chrome_exe="c:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        #        proxy_arg='--proxy-server='+ proxy
        #        chrome_options.add_argument(proxy_arg)        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

        browser = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options)
        browser.implicitly_wait(60)

        return browser


def crawl_list_data(page_no):
    global in_page_num
    global detail_data_list
    list_url = 'http://www.hljcredit.gov.cn/WebCreditQueryService.do?gssearch&type=sxbzxrqg&detail=true&sxbzxrmc=&proselect=&cityselect=&disselect=&curPageNO=' + str(
        page_no)
    #    try:
    br.set_page_load_timeout(15)
    br.get(list_url)  # 页面加载超时设置10秒,出现异常的话, 在异常中判断需要的元素是否加载成功
    time.sleep(10)

    #    except:
    #        try:#如果需要的元素加载成功则继续,否则RETURN FALSE
    #            br.find_element_by_xpath('html/body/div[6]/table/tbody/tr[2]/td[2]/a').get_attribute('text')
    #            pass#未出现异常直接PASS
    #        except:
    #            print('找不到元素')
    ##            br.quit()
    #            raise Exception("找不到元素")

    #    WebDriverWait(br, 10, 1.0).until(EC.presence_of_element_located((By.XPATH,"html/body/div[6]/table/tbody/tr[2]/td[2]/a")))
    #    WebDriverWait(br, 10).until(lambda br:br.find_element_by_xpath("html/body/div[6]/table/tbody/tr[2]/td[2]/a").is_displayed())
    #    print('find element')
    #    detail_data_list=[]
    while in_page_num <= 11:
        # time.sleep(5)
        br.set_page_load_timeout(10)
        time.sleep(10)
        # print(br.page_source)

        click_element = br.find_element_by_xpath('//table[@class="list_2_tab"]/tbody/tr[' + str(in_page_num) + ']//a[1]')
        # print(click_element)
        list_frname = br.find_element_by_xpath('//table[@class="list_2_tab"]/tbody/tr[' + str(in_page_num) + ']//a[1]').get_attribute('title').strip()
        list_cidno = br.find_element_by_xpath("//tbody/tr[" + str(in_page_num) + "]/td[3]").text.replace(' ', '')
        # print(list_frname, list_cidno)
        time.sleep(10)
        try:
            click_element.click()
            time.sleep(10)
        except Exception as e:
            print(e)
            print('cannot find element to click,change proxy')
        #            br.quit()
        #            raise Exception("cannot find element to click,change proxy")

        #        href=br.find_element_by_xpath("html/body/div[6]/table/tbody/tr["+str(i)+"]/td[2]/a").get_attribute('href')
        #        br.get(href)
        #        print(href)

        #        print(br.window_handles)

        handles = br.window_handles

        try:
            br.switch_to.window(handles[1])
        except:
            #            print('切换窗口错误')
            raise Exception("切换窗口错误")

        try:

            WebDriverWait(br, 10, 10).until(
                EC.presence_of_element_located((By.XPATH, '//td[contains(text(),"发布时间")]')))

            detail_data = get_detail(br.page_source, page_no, list_frname, list_cidno)
            print(detail_data)
            br.close()
            br.switch_to.window(handles[0])
            detail_data_list.append(detail_data)
            in_page_num += 1
            time.sleep(10)
        except:
            #            print('detail load time out,change proxy')
            #            br.quit()
            raise Exception("detail load time out,change proxy")
        #        WebDriverWait(br, 10, 1.0).until(EC.presence_of_element_located((By.XPATH,"//td[contains(text(),'身份证号')]/following-sibling::td/text()")))
    #        detail_data=get_detail(br.page_source,page_no,list_frname,list_cidno)
    #        br.close()
    #        br.switch_to_window(handles[0])
    #        detail_data_list.append(detail_data)
    #        in_page_num+=1
    #    in_page_num=2
    #        print(br.page_source)

    #        except:

    return []


#        br.switch_to_window(handles[1])
#        break


def get_detail(page_source, page_no, list_frname, list_cidno):
    root = etree.HTML(page_source)
    ah, qyfr, xb, nl, sfzh, qyfr2, dymc, zxfy, zxyjwh, zczxyjdw, bzxrdlxqk, sxbzxrjtqx, ylvbf, wlvbf, lasj, fbsj = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
    if root.xpath('//td[contains(text(),"身份证号")]/following-sibling::td/text()') == []:
        print('无详情数据数据')
        qyfr = list_frname
        sfzh = list_cidno
    else:
        qyfr = root.xpath('//td[contains(text(),"企业法人")][1]/following-sibling::td/text()')
        sfzh = root.xpath('//td[contains(text(),"身份证号")]/following-sibling::td/text()')

    ah = root.xpath('//td[contains(text(),"案号")]/following-sibling::td/text()')
    xb = root.xpath('//td[contains(text(),"性别")]/following-sibling::td/text()')
    nl = root.xpath('//td[contains(text(),"年龄")]/following-sibling::td/text()')

    qyfr2 = root.xpath('//td[contains(text(),"企业法人")][2]/following-sibling::td/text()')
    dymc = root.xpath('//td[contains(text(),"地域名称")]/following-sibling::td/text()')
    zxfy = root.xpath('//td[contains(text(),"执行法院")]/following-sibling::td/text()')

    zxyjwh = root.xpath('//td[contains(text(),"执行依据文号")]/following-sibling::td/text()')
    zczxyjdw = root.xpath('//td[contains(text(),"作出执行依据单位")]/following-sibling::td/text()')
    bzxrdlxqk = root.xpath('//td[contains(text(),"被执行人的履行情况")]/following-sibling::td/text()')
    sxbzxrjtqx = root.xpath('//td[contains(text(),"失信被执行人具体情形")]/following-sibling::td/text()')

    ylvbf = root.xpath('//td[contains(text(),"已履行部分")]/following-sibling::td/text()')
    wlvbf = root.xpath('//td[contains(text(),"未履行部分")]/following-sibling::td/text()')
    lasj = root.xpath('//td[contains(text(),"立案时间")]/following-sibling::td/text()')
    fbsj = root.xpath('//td[contains(text(),"发布时间")]/following-sibling::td/text()')

    ah = hclear(ah)
    qyfr = hclear(qyfr)
    xb = hclear(xb)
    nl = hclear(nl)

    sfzh = hclear(sfzh)
    qyfr2 = hclear(qyfr2)
    dymc = hclear(dymc)
    zxfy = hclear(zxfy)

    zxyjwh = hclear(zxyjwh)
    zczxyjdw = hclear(zczxyjdw)
    bzxrdlxqk = hclear(bzxrdlxqk)
    sxbzxrjtqx = hclear(sxbzxrjtqx)

    ylvbf = hclear(ylvbf)
    wlvbf = hclear(wlvbf)
    lasj = hclear(lasj)
    fbsj = hclear(fbsj)
    current_time = time.strftime('%Y/%m/%d', time.localtime(time.time()))
    #    print(ah,qyfr,xb,nl,sfzh,qyfr2,dymc,zxfy,zxyjwh,zczxyjdw,bzxrdlxqk,sxbzxrjtqx,ylvbf,wlvbf,lasj,fbsj)
    detail_data = {'case_no': ah, 'frname1': qyfr, 'gender': xb, 'age': nl, 'cidno': sfzh, 'frname2': qyfr2,
                   'area': dymc, 'exec_court': zxfy,
                   'exec_accroding_to': zxyjwh, 'exec_accroding_department': zczxyjdw, 'fulfill_status': bzxrdlxqk,
                   'fulfill_detail_info': sxbzxrjtqx,
                   'fulfilled': ylvbf, 'not_fulfill': wlvbf, 'file_time': lasj, 'pub_time': fbsj,
                   'crawl_time': current_time, 'page_no': page_no}
    print(qyfr)
    return detail_data


def hclear(x):
    x2 = ''
    for x0 in x:
        x0 = x0.replace('\xa0', '').replace('\r', '').replace('\n', '').replace('\t', '')
        x2 += x0

    return (x2)


# %% 获取代理
def getip():
    proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format()
    count = 0
    while count < 100000:
        try:
            ipreq = requests.get(proxyurl, timeout=10)
            ipcontent = ipreq.content
            ipcontent = simplejson.loads(ipcontent)
            hip = ipcontent['ip']
            hport = ipcontent['port']
            hproxy = str(hip) + ':' + str(hport)
            return hproxy
        except:
            count += 1
            print('代理获取失败,重试' + str(count))
            time.sleep(1)


# %% 写数据库
def write_database(detail_data):
    count = 1
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456z', db='db_parker', charset='utf8')
    for detail in detail_data:
        table = 'hlj_shixin'
        qmarks = ', '.join(['%s'] * len(detail))  # 用于替换记录值
        cols = ', '.join(detail.keys())  # 字段名
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, qmarks)
        #        sql='select * from %s limit 10' % table
        #        cursor=db.cursor()
        #        cursor.execute(sql)
        #        cursor.fetchall()
        data_value = list(detail.values())
        cursor = db.cursor()
        try:
            cursor.execute(sql, data_value)
        except:
            print('execute sql error!')
            cursor.close()
            db.close()
            return False

        count += 1
    db.commit()
    #    cursor.close()
    db.close()
    print('写入了%d条数据' % len(detail_data))
    return True


def write_pageno(pageno, filepath):
    output = open(filepath, 'w')
    output.write(str(page_no))
    output.close()


def read_pageno(filepath):
    f = open(filepath, 'r')
    page_no = f.readline()
    f.close()
    return page_no


# %%
if __name__ == "__main__":
    #    proxy=getip()
    #    br=get_web_driver("chrome_with_proxy",proxy)
    ##    wait = WebDriverWait(br, 20, 1.0)
    #    br.set_page_load_timeout(10)
    #    br.set_script_timeout(30)
    #    br=get_web_driver("chrome_noproxy")
    page_no_file='hlj_pageno.txt'
    page_no=int(read_pageno(page_no_file))
    page_no = 1
    global in_page_num
    in_page_num = 2
    global detail_data_list
    flag = True  # 用来停止程序
    #    detail_data_list=[]
    detail_data_list = []
    proxy = getip()
    br = get_web_driver("chrome_noproxy", proxy)
    while flag and page_no <= 2000000:
        print(page_no)
        #        print('in_page_num'+str(in_page_num))
        #        print(detail_data_list)
        #        crawl_list_data(br,page_no)
        if (len(detail_data_list) < 10):

            try:
                detail_flag = crawl_list_data(page_no)
            except Exception as err:
                print(err)
                br.quit()
                proxy = getip()
                br = get_web_driver("chrome_noproxy", proxy)
                continue
        #            try:
        #                br.quit()
        #            except:
        #                continue
        else:
            pass

        if (len(detail_data_list) >= 10):
            write_database(detail_data_list)
            detail_data_list = []
            write_pageno(page_no, page_no_file)
            page_no += 1
            in_page_num = 2
        #            br.close()
        else:
            continue

#        if page_no == 1582:
#            break
#        else:
#            pass
#    else:
#        print('flag is False')
# 此处拿到了简情的信息
#    brief_list=crawl_list_data(page_no)
# 使用浏览器去爬取详情
