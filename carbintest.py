# -*- coding: utf-8 -*-
import json

import pymongo
import requests
import pymysql
import redis
import logging

logger = logging.getLogger()  # 不加名称设置root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
'%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
# 使用FileHandler输出到文件
log_file = 'carbin_log'
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
# 使用StreamHandler输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
# 添加两个Handler
logger.addHandler(ch)
logger.addHandler(fh)


logger =logging.getLogger()


conn = pymysql.connect(host='10.18.6.101', port=3306, user='case_dev', passwd='pass123', db='spider',
                       charset='utf8')
cursor = conn.cursor()
proxy_rds = redis.StrictRedis('10.18.6.102', db=13,decode_responses=True)
doc = pymongo.MongoClient('10.18.6.102', port=27018)['spider']['cardbin_history']


def proxies():
    proxy = proxy_rds.randomkey()
    # print('使用代理{}'.format(proxy))
    proxy_dict = {'https': 'https://{}'.format(proxy)}
    return proxy_dict


def get_html(page, card):
    data = {
        "limit": "500",
        "offset": str(page),
        "sortOrder": "asc",
        "inputValue": card,
    }
    url = 'https://cha.zfzj.cn/bankCardDetail/select'
    headers = {
        "Host": "cha.zfzj.cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://cha.zfzj.cn/mainPage.html",
    }
    retry =10
    count =0
    while count < retry:
        proxy = proxies()

        try:
            # print(proxy)
            r = requests.post(url, data=data, headers=headers, proxies=proxy,timeout=15)
        except Exception as e:
            logger.error('异常 >>>> {}'.format(e))
            count+=1
            logger.info('>>>> 重试第{}次'.format(count))
            continue
        else:
            if r.status_code==200:
                return r.text
            else:
                count += 1
                logger.warning('返回状态码不为200，实际为{}'.format(r.status_code))
                continue
    logger.warning('重试超过10次，退出当前查询')
    return None

def todb(card, html):
    js = json.loads(html)
    rows = js['rows']
    if not rows:
        return
    for row in rows:
        accountLength = row['accountLength']
        cardName = row['cardName']
        cardType = row['cardType']
        mainAccount = row['mainAccount']
        mainValue = row['mainValue']
        orgName = row['orgName']
        sql = "insert into card_bin (accountLength,card,cardName,cardType,mainAccount,mainValue,orgName) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(
            accountLength, card, cardName, cardType, mainAccount, mainValue, orgName);
        try:
            cursor.execute(sql)
            conn.commit()
            doc.update_one({'cardno':card},{'$set':{'status':1}})
            # update_sql = "update cardno_temp set status=1 where cardno='{0}'".format(card)
            # cursor.execute(update_sql)
            # conn.commit()
            logger.info('success:' + card)
        except Exception as e:
            doc.update_one({'cardno':card},{'$set':{'status':-1}})

            logger.info('fail:' + card)
            logger.error('入库失败，错误信息:{}'.format(e))
            conn.rollback()



def get_name_redis():
    r = redis.StrictRedis('10.18.6.102',db=7,decode_responses=True)

    while 1:
        card= r.lpop('cardbin0925')
        logger.info('card >>> {}'.format(card))
        if card:
            doc.insert({'cardno': card, 'status': -999})
            # time.sleep(5)
            html = get_html(1, card)
            if not html:
                logger.info('html为None，需要重试的页面')
                doc.update_one({'cardno': card}, {'$set': {'status': -1}})

                continue
            try:
                js = json.loads(html)
            except Exception as e:
                logger.error('json异常，异常信息{}'.format(e))
                # print(e)
                # 异常记录下来，稍后重试
                continue

            total = js['total']
            if total == 0:

                doc.update_one({'cardno': card}, {'$set': {'status': 0}})
                continue

            pages = int(total / 500) if total % 500 == 0 else int(total / 500) + 1
            todb(card, html)

            if pages > 1:
                for page in range(2, pages + 1):
                    html = get_html(page, card)
                    if not html:
                        logger.info('翻页时候，html为None，需要重试的页面')
                        doc.update_one({'cardno': card}, {'$set': {'status': -1}})
                        continue
                    todb(card, html)
        else:
            break


def save_name_redis():
    r = redis.StrictRedis('10.18.4.211',db=10,decode_responses=True)
    card_list = []
    with open('cardbin.txt','r') as f:
        while 1:
            line  = f.readline()
            if line:
                insert_item = line.strip()

                card_list.append(insert_item)
            else:
                break

    ret = list(set(card_list))
    for i in ret:
        r.lpush('cardbin0927',i)



if __name__ == "__main__":
    # get_name_redis()
    # mysql()
    save_name_redis()