# -*- coding: utf-8 -*-
import pymongo
import requests
import simplejson as simplejson
import pymysql
import redis

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider',
                       charset='utf8')
cursor = conn.cursor()
rds = redis.StrictRedis('10.18.6.102', db=13)
doc = pymongo.MongoClient('10.18.6.102', port=27018)['spider']['cardbin_history']


def proxies():
    proxy = rds.randomkey()
    # print('使用代理{}'.format(proxy))
    proxy_dict = {'http': 'http://{}'.format(proxy)}
    return proxy_dict


def get_html(page, card):
    data = {
        "limit": "500",
        "offset": str(page),
        "sortOrder": "asc",
        "inputValue": card
    }
    proxy = proxies()
    url = 'https://cha.zfzj.cn/bankCardDetail/select'
    headers = {
        "Host": "cha.zfzj.cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://cha.zfzj.cn/mainPage.html",
    }
    index_html = ''
    try:
        r = requests.post(url, data=data, allow_redirects=False, headers=headers, timeout=30, proxies=proxy)
    except Exception as e:
        print(e)
        get_html(page, card)
    else:
        if r.status_code == 200:
            index_html = r.text
            return index_html
        else:
            print(str(r.status_code))
            get_html(page, card)


def todb(card, html):
    json = simplejson.loads(html)
    rows = json['rows']
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
            print('success:' + card)
        except:
            doc.update_one({'cardno':card},{'$set':{'status':-1}})

            print('fail:' + card)
            conn.rollback()



def get_name_redis():
    r = redis.StrictRedis('10.18.6.102',db=7,decode_responses=True)

    while 1:
        card= r.lpop('cardbin')
        if card:
            doc.insert({'carno': card, 'status': -999})

            html = get_html(1, card)
            if not html:
                doc.update_one({'cardno': card}, {'$set': {'status': -1}})

                continue

            json = simplejson.loads(html)
            total = json['total']
            if total == 0:
                doc.update_one({'cardno': card}, {'$set': {'status': 0}})

                continue
            pages = int(total / 500) if total % 500 == 0 else int(total / 500) + 1
            todb(card, html)
            if pages > 1:
                for page in range(2, pages + 1):
                    html = get_html(page, card)
                    if not html:
                        doc.update_one({'cardno': card}, {'$set': {'status': -1}})

                        continue
                    todb(card, html)




def save_name_redis():
    r = redis.StrictRedis('10.18.6.102',db=7,decode_responses=True)
    card_list = []
    with open('cardbin.txt','r') as f:
        while 1:
            line  = f.readline()
            if line:
                card_list.append(line.strip())
            else:
                break

    ret = list(set(card_list))
    for i in ret:
        r.lpush('cardbin',i)



if __name__ == "__main__":
    # get_name_redis()
    # mysql()
    save_name_redis()