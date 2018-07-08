# -*-coding=utf-8-*-
import codecs
import re
import sys
import requests, urllib2, urllib, json
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
def using_requests():
    post_data = {'first': 'true', 'kd': 'Android', 'pn': '1'}
    url = "http://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"
    r = requests.post(url, data=post_data)
    #r=requests.post("http://www.lagou.com/jobs/positionAjax.json?px=default",data=post_data)
    print(r.text)


def getJson():
    user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    headers = {"User-Agent": user_agent}
    url = "http://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"

    data = {"first": "false", "pn": "2", "kd": "Python"}
    post_data = urllib.urlencode(data)
    req = urllib2.Request(url, headers=headers, data=post_data)

    resp = urllib2.urlopen(req)
    return_data = resp.read()
    print(return_data.decode("utf-8"))
    f = open("json.txt", 'w')
    f.write(return_data)
    f.close()
    json_data = json.loads(return_data)
    print(type(json_data))
    #print(json_data['success'])
    #print(json)

#using_requests()


def jsonParse(dictionary):
        if isinstance(dictionary,dict):
            for i in range(len(dictionary)):
                key=dictionary.keys()[i]
                value=dictionary[key]
                print(key,value)

                jsonParse(value)


def list_all_dict(dict_a):
    if isinstance(dict_a, dict):  # 使用isinstance检测数据类型

        for x in range(len(dict_a)):
            temp_key = dict_a.keys()[x]

            temp_value = dict_a[temp_key]

            print"%s : %s" % (temp_key, temp_value)

            list_all_dict(temp_value)  # 自我调用实现无限遍历

def testcase1():
    new_url = 'http://api.k.sohu.com/api/channel/v6/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=1&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553053&cdma_lng=113.902393&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=9bf84c6c9d24711f43f7058db2d1ed5ba7c6a2fecca504d3f44839a8bf22b4521ff192a4ac2d77946d871706ceb89baa269d145d2f5a07fddb656d6417029bb04459d2a5aa0ca50764b2de62da32f9e5e6055efa78b93cafbd89ef0971a836d3542ce2065edff7017a28b164e4210fec&v=1502985600&t=1503044087&page=1&action=0&mode=0&cursor=0&mainFocalId=0&focusPosition=1&viceFocalId=0&lastUpdateTime=0&gbcode=440300&forceRefresh=0&apiVersion=37&u=1&source=0&isSupportRedPacket=0&t=1503044087'

    s=requests.get(new_url)
    js=s.json()
    #print(js)
    list_all_dict(js)

def testcase2():
    js=json.loads(open('lianjia_sh.txt').read())
    #print(js)
    body=js['data']
    tree = etree.HTML(body)
    nodes = tree.xpath('//li[@class="pictext"]')
    print("NODE:",len(nodes))
    print(js['args'])
    print('*'*20)
    print(type(js))
    print(type(js['args']))
    #p=re.compile('"cur_city_name":"(.*?)"')
    p=re.compile('"total":(\d+)')
    s=p.findall(js['args'])[0]
    print(s)
    '''
    print(type(s))
    print(s)
    print(s.decode('utf-8').encode('gbk'))
    print(s.decode('unicode_escape'))

    
    for k,v in js['args'].items():
        print(k,"::",v)
    '''

def read_lj():
    #js = json.loads(open('lianjia_sh.txt').read())
    js = json.loads(open('lianjia_sz.txt').read())
    arg= json.loads(js['args'])
    print(arg['no_more_data'])
    '''
    all=js['data']['list']
    #print(all)
    print(len(all))
    for i in all:
        if i.has_key('completeYear'):
            print(i['completeYear'])
        
        print(i['referAvgPrice'])
        print(i['houseType'])
        print(i['completeYear'])
        
        #print(i[''])
        
        for k,v in i.items():
            print(k,v)
        print('*'*10)
   
    '''

def json_read_file():
    fp=codecs.open('city_list.txt')
    data=fp.read()
    js=json.loads(data)
    d=dict()
    for k,v in js.items():
        #print(k)
        short_cut= v['url'].split('/')[3]
        d[short_cut]=k
    print(d)
    str1=json.dumps(d,ensure_ascii=False)
    fp2=codecs.open('new_city.txt','w',encoding='utf-8')
    fp2.write(str1)
    fp2.close()


#getJson()
#testcase1()
#testcase2()
#read_lj()
json_read_file()
