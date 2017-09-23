# coding: utf-8
import json
import time
import datetime

import requests


def getheader():
    with open('request_header') as fp:
        data = fp.readlines()
    dictionary = dict()
    for line in data:
        line = line.strip()
        dictionary[line.split(":")[0]] = ':'.join(line.split(":")[1:])
    return dictionary


def analysis_cookie():
    cookie = getheader()['Cookie']
    for item in items:
        name = item.split('=')[0]
        value = item.split('=')[1]
        print name, " : ", value


def urlParse():
    url='https://lf.snssdk.com/api/news/feed/v66/?category=news_astrology&concern_id=6215497898268822018&refer=2&count=10&max_behot_time=1506047993&last_refresh_sub_entrance_interval=1506149205&loc_mode=0&loc_time=1505991427&latitude=22.553074&longitude=113.902542&city=%E6%B7%B1%E5%9C%B3%E5%B8%82&tt_from=pre_load_more&lac=42360&cid=45370605&cp=5395c04f7ccb5q1&plugin_enable=3&iid=15189530186&device_id=38220008232&ac=wifi&channel=smartisan&aid=13&app_name=news_article&version_code=636&version_name=6.3.6&device_platform=android&ab_version=169863%2C177250%2C179334%2C173967%2C172663%2C172659%2C171194%2C176916%2C170349%2C178991%2C176179%2C177070%2C169447%2C178210%2C179194%2C168463%2C174398%2C178732%2C178921%2C169300%2C178930%2C177166%2C152026%2C176593%2C178581%2C176695%2C177786%2C170713%2C179373%2C176739%2C179006%2C179751%2C156262%2C145585%2C179382%2C174429%2C177258%2C179636%2C177042%2C162572%2C176599%2C176609%2C179625%2C175163%2C169176%2C175634%2C176616%2C170988%2C178989%2C176597%2C176652%2C177702%2C176615&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_feature=102749%2C94563&abflag=3&ssmix=a&device_type=SM801&device_brand=SMARTISAN&language=zh&os_api=22&os_version=5.1.1&uuid=990006203070023&openudid=4dd00e258bbe295f&manifest_version_code=636&resolution=1080'
    x = url.split('&')
    fp = open('urlparse', 'w')
    for i in x:
        print i
        fp.write(i + '\n')
    fp.close()

def urlAdd(filename):
    t = int(time.time())
    with open(filename, 'r') as fp:
        line = fp.readline().strip()
        url = line
        # print url
        curr_d = datetime.datetime.fromtimestamp(t)
        while 1:
            # print url
            line = fp.readline().strip()
            if len(line) < 1:
                break
            sp = line.split('=')
            # print sp[0],sp[1]
            # print arg,val

            if sp[0] == 'channelId':
                url = url + '&' + 'channelId=' + ''
            if sp[0] == 'page':
                url = url + '&' + 'page=' + ''
            if sp[0] == 't':
                url = url + '&' + 't=' + str(t)
            if sp[0] == 'action':
                url = url + '&' + 'action=' + ''
            else:
                url = url + '&' + line
                # print 'done'
    print url
    r = requests.get(url)
    print r.json()

    #return url
    # print url

def read_json():
    fp=open('temp','r').read().strip()
    #js=json.load(fp,encoding='utf-8')

    #print fp
    #js=json.loads(fp)
    #print js
    return_data=eval(fp)
    print return_data
    #print return_data['log_extra']
    if return_data.has_key('app_name'):
        print return_data.get('app_name')
        print return_data.get('title')
        print return_data.get('image')
        print return_data.get('image').get('url')
        print "TS"

    for k,v in return_data.items():
        #print k,v
        if k=='image_list':
            #print v
            for i in v:
                for ik,iv in i.items():
                    if ik=='url_list':
                        picUrl= iv[0].get('url')
                        print picUrl
                        break


        if k=='filter_words':
            for i in v:
                for k1,v1 in i.items():
                    #print k1,v1
                    pass

if __name__ == "__main__":
    #print getheader()
    # analysis_cookie()
    #urlParse()
    #read_json()
    urlAdd('urlparse')
