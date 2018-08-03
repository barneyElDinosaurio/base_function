# -*-coding=utf-8-*-
import pandas as pd
import requests


def get_result(url):
    if len(url)<1:
        return 'URL Error'

    data = {'url': url}
    host = 'http://127.0.0.1:8000/barcode'
    try:
        r = requests.post(url=host,data=data,timeout=10)
        ret = r.json()
    except Exception as e:
        ret = "Timeout"
    print(ret)
    return ret

df = pd.read_csv('qrcode_spider_res.csv')
# print(df.head())
result = []
for index,url in enumerate(df['spider_url'].values):
    print(index,url)
    ret = get_result(url)
    result.append(ret)
df['myresult']=result
df.to_csv('new_result.csv',encoding='utf-8')



