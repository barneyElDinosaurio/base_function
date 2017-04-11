# -*-coding=utf-8-*-
__author__ = 'Rocky'
import requests
code='300333'
stock=dict(stockCode=code)
print stock
def leverfun_data():
    stock_api = 'https://app.leverfun.com/timelyInfo/timelyOrderForm'
    s=requests.get(stock_api,params=stock)
    data= s.json()
    print data
    '''
    for i in data:
        print i,
        print " ",
        print data[i]
    '''
    count=1
    for i in data['data']['sellPankou']:
        print count,'\t',
        print i['price'],"\t",i['volume']
        count=count+1
    print "*"*15

    count=1
    for j in data['data']['buyPankou']:
        print count,'\t',
        print j['price'],"\t",j['volume']
        count=count+1

leverfun_data()