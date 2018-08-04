# -*-coding=utf-8-*-
import pandas as pd
import requests
from sqlalchemy import create_engine
import pymysql
import json
# engine = create_engine('mysql+pymysql://root:123456z@localhost:3306/db_parker?charset=utf8')

def get_result(url):
    if len(url)<1:
        return 'URL Error'
    url=url.split()[0]

    data = {'url': url}
    host = 'http://127.0.0.1:8000/barcode'
    try:
        r = requests.post(url=host,data=data,timeout=10)
        ret = r.json()
    except Exception as e:
        ret = "Timeout"
    print(ret)
    return ret

# df = pd.read_csv('qrcode_spider_res.csv')
# df.to_sql('tb_qrcode',engine)
# print(df.head())
# result = []
# for index,url in enumerate(df['spider_url'].values):
#     print(index,url)
#     ret = get_result(url)
#     result.append(ret)
# df['myresult']=result
# df.to_csv('new_result.csv',encoding='utf-8')

# df = pd.read_sql('tb_qrcode',engine,index_col='index')
# print(df.head())

connect = pymysql.connect(host='localhost',user='root',password='123456z',db='db_parker')
cursor = connect.cursor()
query_cmd = 'select * from tb_qrcode where validation is null'
cursor.execute(query_cmd)
ret = cursor.fetchall()
for item in ret:
    # print(item[0],item[1],item[2],item[3])
    url = item[2]
    ret = get_result(url)
    rets=json.dumps(ret,ensure_ascii=False)
    # print(type(rets))
    update_cmd ='update tb_qrcode set validation = "{}" where `index` = {};'.format(ret,item[0])
    # print(update_cmd)
    try:
        cursor.execute(update_cmd)
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()

connect.commit()

