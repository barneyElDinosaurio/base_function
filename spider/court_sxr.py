# -*-coding=utf-8-*-
# @Time : 2018/9/3 15:12
# @File : court_sxr.py
# @author : chenjinwei
import copy
import random
import re
import requests.adapters
import shutil
import os
import requests
from scrapy.selector import Selector
import base64
import time
import pymongo
import config
from myultility import redis_proxy, random_ua
import redis
import pandas as pd
import math
import logging
import datetime

# from fake_useragent import UserAgent


def llogger(filename):
    pre_fix = os.path.splitext(filename)[0]
    # 创建一个logger
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    current = datetime.datetime.now().strftime('%Y-%m-%d')
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(pre_fix + '-{}.log'.format(current))

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()

    # # 定义handler的输出格式
    formatter = logging.Formatter(
        '[%(asctime)s][Filename: %(filename)s][line: %(lineno)d][%(levelname)s] :: %(message)s')

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数

logger = llogger('court_sxr')

cidno = ''

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
    'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    'Host': 'zxgk.court.gov.cn',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0(WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.22.99Safari'
}

post_header = {
    'Host': 'zxgk.court.gov.cn',
    # 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
    'User-Agent': 'Mozilla/5.0(WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.22.99Safari',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://zxgk.court.gov.cn/shixin/findDis',
    # 'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded'
}

detail_header = {
    'Host': 'zxgk.court.gov.cn',
    # 'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
    'User-Agent': 'Mozilla/5.0(WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.22.99Safari',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://zxgk.court.gov.cn/shixin/new_index.html',
}

url = 'http://zxgk.court.gov.cn/shixin/index_form.do'
post_url = 'http://zxgk.court.gov.cn/shixin/findDis'

mongo = pymongo.MongoClient('10.18.6.26', 27018)
doc = mongo['spider']['sx_ent']


# ua =UserAgent()

# 编码
def img_to_b64(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data.decode('utf-8')


# 接口识别验证码
def crack_code(img_path):
    img_b64 = img_to_b64(img_path)  # 转为base64编码
    img_dict = {'img': img_b64}
    res = requests.post('http://10.18.6.102:5001/Captcha_api', data=img_dict, verify=False, timeout=2)
    return res.text

# 更新session 验证码
def update_session(session, name, cap_id, full_image_url, pageNo=None):
    retry = 1
    while retry < 10:
        logger.info('第{}次更新'.format(retry))
        try:
            png_strean = session.get(full_image_url, headers=headers,
                                     proxies=redis_proxy(),
                                     timeout=12)
            with open('test.png', 'wb') as f:
                f.write(png_strean.content)

        except Exception as e:
            logger.warning('下载图片失败')
            logger.warning(e)
            retry = retry + 1
            continue
            # return session, None

        # 调用接口识别验证码
        codes = crack_code('test.png')

        # 识别出错后重新下载新的图片
        if codes == '100' or codes == '101':
            logger.warning('接口端识别失败或者有干扰线')
            shutil.copy('test.png', 'piaoxian{}.png'.format(int(time.time())))
            retry = retry + 1
            continue
            # return session, None

        # 填充post data
        payloads = {
            'pName': name,
            'pCardNum': cidno,
            'pProvince': '0',
            'pCode': codes,
            'captchaId': cap_id,
        }
        if pageNo:
            payloads['currentPage'] = str(pageNo)

        try:
            resp_content = session.post(url=post_url, data=payloads, headers=post_header,
                                        proxies=redis_proxy(),
                                        timeout=10)
            # print(resp_content.text)

        except Exception as e:
            logger.warning(e)
            logger.warning('提交post数据异常')
            retry = retry + 1
            time.sleep(random.random() * 2)
            continue

        else:

            if '验证码错误或验证码已过期' in resp_content.text:
                logger.warning('识别的验证码和网站不一样')
                shutil.copy('test.png', 'shibiecuowu{}.png'.format(int(time.time())))
                retry = retry + 1
                continue
                # return session, codes, None

            return session, codes, resp_content

    codes = '100'
    return session, codes, None


# 360安域反爬
def anti_anyu(name):
    session = requests.Session()
    session.keep_alive = False  # 关闭多余连接
    try:
        logger.info('获取查询页面')
        get_session = session.get(url=url, headers=headers,
                                  proxies=redis_proxy(),
                                  timeout=5)
    except Exception as e:
        logger.warning(e)
        logger.info('>>>> 获取查询页失败')
        return None
    # print(get_session.text)

    response = Selector(text=get_session.text)
    image_url = response.xpath('//img[@id="captchaImg"]/@src').extract_first()

    logger.info('>>>>从查询页面获取图片captchaImg 和url {}'.format(image_url))
    try:
        cap_id = re.search('captchaId=(.*?)&', image_url).group(1)
    except Exception as e:
        logger.warning(e)
        logger.warning('>>>>没有找到captchaId')
        return None

    full_image_url = 'http://zxgk.court.gov.cn/shixin/' + image_url

    for _ in range(10):
        session, code, resp_content = update_session(session, name, cap_id, full_image_url)
        if resp_content:
            break

    return session


# 查询一个名字
def check_sxr(name):
    '''
    :param name: 查询的个人名字/企业名字
    :return: -1 访问出错；0：无查询记录，大于0：有查询记录，返回条数
    '''

    session = requests.Session()
    session.keep_alive = False  # 关闭多余连接
    item_num = 0
    custom_ua = random_ua()
    headers['User-Agent'] = custom_ua
    post_header['User-Agent'] = custom_ua
    detail_header['User-Agent'] = custom_ua

    try:
        logger.info('获取查询页面')
        get_session = session.get(url=url, headers=headers,
                                  proxies=redis_proxy(),
                                  timeout=10)
    except Exception as e:
        logger.warning(e)
        logger.info('>>>> 获取查询页失败')
        return -1, -1
    # print(get_session.text)

    response = Selector(text=get_session.text)
    image_url = response.xpath('//img[@id="captchaImg"]/@src').extract_first()

    logger.info('>>>>从查询页面获取图片captchaImg 和url {}'.format(image_url))
    try:
        cap_id = re.search('captchaId=(.*?)&', image_url).group(1)
    except Exception as e:
        logger.warning(e)
        logger.warning('>>>>没有找到captchaId')
        return -1, -1

    full_image_url = 'http://zxgk.court.gov.cn/shixin/' + image_url

    # 重试10次
    for _ in range(10):
        session, code, resp_content = update_session(session, name, cap_id, full_image_url)
        if resp_content:
            break

    if not resp_content:
        logger.warning('>>>>获取的内容为空')
        return -1, -1

    try:
        count_number = int(re.search('共(\d+)条', resp_content.text).group(1))
    except Exception as e:
        logger.warning(e)
        logger.warning('>>>>页面内容为空,条数没找到')
        count_number = 0

    if count_number == 0:
        logger.warning('>>>>无此人/企业实行记录')
        return 0, 0

    # 页面数目
    total_page = int(math.ceil(count_number / 10))

    # for p in range(1, total_page + 1):
    p = 1
    while p < total_page + 1:
        payload_page = {
            'currentPage': str(p),
            'pName': name,
            'pCardNum': cidno,
            'pProvince': '0',
            'pCode': code,
            'captchaId': cap_id,
        }

        try:
            # 需要把header remove
            # 这个时候会过期
            logger.info('>>>> 提交翻页请求,页码：{}'.format(p))
            proxy_ip = redis_proxy()
            logger.info('目前的代理IP是 前：{}'.format(proxy_ip))
            resp_content = session.post(url=post_url, data=payload_page, headers=post_header,
                                        proxies=proxy_ip,
                                        timeout=10
                                        )
            logger.info('目前的代理IP是：{}'.format(proxy_ip))
            # print(resp_content.text)
        except Exception as e:
            logger.warning(e)
            logger.warning('>>>>提交post数据异常')
            continue

        else:
            if '验证码错误或验证码已过期' in resp_content.text:
                logger.warning('识别的验证码和网站不一样')

                for _ in range(10):
                    # 下载图片
                    logger.info('>>>> 下载图片，更新session')
                    session, code, resp_content = update_session(session, name, cap_id, full_image_url, p)
                    if resp_content:
                        break
            if not resp_content:
                return -1, -1

            if '已被安域防护拦截' in resp_content.text or '屏蔽' in resp_content.text:
                logger.warning('>>>>被安域防护拦截')
                for _ in range(5):

                    session = anti_anyu()
                    if session:
                        break
                continue

            if not resp_content:
                return -1, -1

            response = Selector(text=resp_content.text)
            t = response.xpath('//table[@class="Resultlist"]/tbody/tr')[1:]

            item_len = len(t)
            index = 0
            retry_num = 0
            retry_max = 20
            # 获取细节
            while index < item_len:
                case_id = t[index].xpath('.//a[@class="View"]/@id').extract_first()
                detail_url = 'http://zxgk.court.gov.cn/shixin/disDetail?id={}&pCode={}&captchaId={}'.format(case_id,
                                                                                                            code,
                                                                                                            cap_id)
                # 失败了重试
                try:
                    logger.info('>>>>获取个人细节')
                    s4 = session.get(url=detail_url, headers=detail_header,
                                     proxies=redis_proxy(),
                                     timeout=5)
                except Exception as e:
                    logger.warning(e)
                    logger.info('重试，设置超时10s')
                    last_try = False
                    for t_out in range(5):
                        time.sleep(random.random() * 2)
                        try:
                            s4 = session.get(url=detail_url, headers=detail_header,
                                             proxies=redis_proxy(),
                                             timeout=10 + t_out)
                            last_try = True
                            break
                        except Exception as e:
                            logger.warning(e)
                            logger.warning('重试失败 :: {}'.format(t_out))
                    if last_try == False:
                        return -1, -1
                    # continue
                if s4.status_code != 200:
                    logger.warning('response error >>>{}'.format(s4.status_code))
                    retry_num = retry_num + 1
                    # return -1
                try:

                    print('>>>> s4内容 {}'.format(s4.text))
                    ret = s4.json()
                except Exception as e:
                    logger.warning(e)
                    logger.warning('>>>> 没获取到json数据')
                    s4.encoding = 'utf8'
                    print()
                    print(s4.text)
                    # 需要重新post 那里 开始

                    session, code, resp_content = update_session(session, name, cap_id, full_image_url)
                    # session, resp_content, code = update_session(session, name,cap_id, full_image_url,pageNo=p)
                    payload_page = {
                        'currentPage': str(p),
                        'pName': name,
                        'pCardNum': cidno,
                        'pProvince': '0',
                        'pCode': code,
                        'captchaId': cap_id,
                    }
                    logger.info('payload 内容 {}'.format(payload_page))
                    try:
                        resp_content = session.post(url=post_url, data=payload_page, headers=post_header,
                                                    # proxies=proxy_ip,
                                                    timeout=10
                                                    )
                    except Exception as e:
                        logger.warning('重新请求的时候出错了')
                        logger.warning(e)

                    logger.info('resp_content {}'.format(resp_content))
                    # 改用while 保持在原页面上操作

                    retry_num + 1
                    continue

                if len(ret) == 0:
                    logger.warning('>>>>返回的json长度为0')
                    session, code, resp_content = update_session(session, name, cap_id, full_image_url)
                    payload_page = {
                        'currentPage': str(p),
                        'pName': name,
                        'pCardNum': cidno,
                        'pProvince': '0',
                        'pCode': code,
                        'captchaId': cap_id,
                    }
                    logger.info('重新post页面数据')
                    logger.info('payload_page 内容 {}'.format(payload_page))
                    try:
                        resp_content = session.post(url=post_url, data=payload_page, headers=post_header,
                                                    # proxies=proxy_ip,
                                                    timeout=5
                                                    )
                    except Exception as e:
                        logger.warning('>>>> 重新提交的时候出错了')
                        logger.warning(e)

                    logger.info('resp_content 返回的内容{}'.format(resp_content))

                    # session, resp_content, code = update_session(session, name,cap_id, full_image_url,pageNo=p)
                    # 改用while 保持在原页面上操作
                    retry_num = retry_num + 1
                    continue

                logger.warning('返回的json数据>>>>>{}'.format(ret))

                doc.insert(ret)
                item_num = item_num + 1
                logger.info('>>>>插入mongodb数据库成功')

                index = index + 1
                # 超过最大的重试次数
                if retry_num > retry_max:
                    break

            p = p + 1

    if count_number != item_num:
        logger.info('>>>>姓名丢失数据{}条'.format(count_number - item_num))
    return item_num, count_number


def get_name_from_redis():
    r = redis.StrictRedis('10.18.6.26', decode_responses=True, db=3)
    # r2 = redis.StrictRedis('10.18.6.102', decode_responses=True, db=8)
    key = 'location_remain'
    mongo_result = pymongo.MongoClient('10.18.6.26', 27018)
    save_doc = mongo_result['spider']['ent_history']
    while 1:
        name = r.lpop(key)
        if name:
            save_doc.insert({'name': name, 'counts': -999})
            logger.info('>>>>查询 地区{}'.format(name))
            item_num, count_number = check_sxr(name)
            # 重试

            stop_count = 10
            current_count = 0
            while (item_num == -1) and (current_count < stop_count):
                item_num, count_number = check_sxr(name)
                current_count = current_count + 1

            # d = {'name': name, 'crawl_count': item_num, 'counts': count_number}
            try:
                save_doc.update({'name': name}, {'$set': {'counts': count_number, 'crawl_count': item_num}},False,True)
            except Exception as e:
                logger.warning(e)

        else:
            break


# name = ''
# item_num, count_number = check_sxr(name)
# print(item_num, count_number)
# push_name_redis()
get_name_from_redis()
# push_excel_redis()
