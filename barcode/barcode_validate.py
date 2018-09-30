# -*-coding=utf-8-*-
import pandas as pd
import re
import requests
from sqlalchemy import create_engine
import pymysql
import json


# engine = create_engine('mysql+pymysql://root:@localhost:3306/db_parker?charset=utf8')

def get_result(url):
    if len(url) < 1:
        return 'URL Error'
    url = url.split()[0]

    data = {'url': url}
    host = 'http://10.18.6.101:9000/barcode'
    try:
        r = requests.post(url=host, data=data, timeout=10)
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

def get_collection():
    connect = pymysql.connect(host='localhost', user='root', password='', db='db_parker', charset='utf8')
    cursor = connect.cursor()
    query_cmd = 'select * from tb_qrcode'
    cursor.execute(query_cmd)
    ret = cursor.fetchall()
    for item in ret:
        # print(item[0],item[1],item[2],item[3])
        url = item[2]
        ret = get_result(url)
        rets = json.dumps(ret, ensure_ascii=False)
        # print(type(rets))
        update_cmd = 'update tb_qrcode set validation4 = "{}" where `index` = {};'.format(ret, item[0])
        # print(update_cmd)
        try:
            cursor.execute(update_cmd)
            connect.commit()
        except Exception as e:
            print(e)
            connect.rollback()

    connect.commit()


def get_static():
    connect = pymysql.connect(host='localhost', user='root', password='123456z', db='db_parker', charset='utf8')
    cursor = connect.cursor()
    query_cmd = 'select * from tb_qrcode'
    cursor.execute(query_cmd)
    ret = cursor.fetchall()
    count = 0
    sibai = 0
    not_valid = 0
    data_none = 0
    fail_get_web = 0
    passed = 0
    failure_one = 0
    shougong = 0
    chaoshi=0

    for item in ret:
        # print(item[0])
        # item[0] 为 0
        if item[7] == 'Timeout':
            host_url = item[2]
            if re.search('www.szcredit.com',host_url):
                count = count + 1

        else:
            pattern = re.compile('\s+')
            rets = pattern.sub('', item[7])
            js = eval(rets)
            msg = js.get('msg')
            datas = js.get('data')
            if msg is not None and msg == '成功':
                passed += 1
                # print(item[2],item[5])
                # item[5]
                # print(item[0])
                # del_cmd = 'delete from `tb_qrcode_copy1` where `index` = {}'.format(item[0])
                # cursor.execute(del_cmd)
                try:
                    pass
                    # connect.commit()
                except Exception as e:
                    print(e)
                    connect.rollback()

                if not datas.get('credit_code') and not datas.get('registered_code'):
                    # print(item[5])
                    failure_one += 1

            if msg is not None and msg == '页面无法打开':
                # del_cmd = 'delete from `tb_qrcode_copy1` where `index` = {}'.format(item[0])
                # cursor.execute(del_cmd)
                sibai += 1

            if msg is not None and msg == '超时':
                chaoshi += 1
                # del_cmd = 'delete from `tb_qrcode_copy1` where `index` = {}'.format(item[0])
                # cursor.execute(del_cmd)
                # print(item[2], item[4], item[5],item[6])

            if msg is not None and msg == '需要手工识别':
                shougong += 1
                # print(item[2], item[4], item[5],item[6])
                # del_cmd = 'delete from `tb_qrcode_copy1` where `index` = {}'.format(item[0])
                # cursor.execute(del_cmd)

            if msg is not None and msg == '没有识别到合法的url':
                not_valid += 1
                # continue
                # del_cmd = 'delete from `tb_qrcode_copy1` where `index` = {}'.format(item[0])
                # cursor.execute(del_cmd)

            if msg is None:
                data_none += 1

            # if msg is not None and datas.get('result') is not None:
            #     if datas.get('result') == 'Failedtogetwebsite':
            #         fail_get_web += 1
            try:
                pass
                # connect.commit()
            except Exception as e:
                print(e)
                connect.rollback()

    print('Timeout ', count)
    print('页面无法打开', sibai)
    print('成功', passed)
    print('没有识别到合法的url', not_valid)
    print('data none', data_none)
    print('fake pass', failure_one)
    print('手工识别', shougong)
    print('超时', chaoshi)


def test_dict():
    txt = {'orderNo': '1533489885186zuyprwsfkmovbqcjl',
           'data': {'credit_code': '91440101MA59EC927R', 'registered_code': '440106001642411',
                    'enterprise_name': '广州德宗文化艺术有限公司', 'enterprise_type': '有限责任公司(自然人投资或控股)',
                    'registered_capital': '300.0000万元人民币', 'built_date': '2016-08-19', 'registered_date': None,
                    'registration_status': '开业状态', 'legal_person': '陈伟雄', 'operator': None, 'operating_from': None,
                    'operating_to': None, 'registration_authority': '广州市越秀区工商行政管理局', 'date_approved': '2018-01-04',
                    'address': '广州市越秀区水荫路35号5栋自编102室',
                    'business_scope': '商事主体的经营范围由章程或协议等文件规定，请查阅章程或协议。以下内容仅供参考：文学、艺（美）术经纪代理服务;照明灯光设计服务;舞台灯光、音响设备安装服务;广告业;新闻业;动漫（动画）经纪代理服务;灯光设备租赁;文化娱乐经纪人;影视经纪代理服务;软件开发;信息技术咨询服务;工艺美术品零售;照相器材出租服务;娱乐设备出租服务;'},
           'status': 1, 'msg': '成功'}
    print(type(txt))
    print(txt.get('msg'))

def delete_test():
    pass

# get_collection()
get_static()
# test_dict()
