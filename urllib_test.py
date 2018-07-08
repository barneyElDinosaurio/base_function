__author__ = 'rocchen'
# -*-coding=utf-8-*-

import urllib2, re, sys

reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2, re, sys, sqlite3, time


#修改成类的方法
class Myurllib2():
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        self.header = {"User-Agent": self.user_agent}

    def proxy_test(self):
        url = "http://httpbin.org/ip"
        dbname = "C://git/getProxy/proxy.db"
        try:
            conn = sqlite3.connect(dbname)
        except:
            print("error")
            return
        query_cmd = '''
        select * from PROXY
        '''
        #设置代理
        cursor = conn.execute(query_cmd)
        for row in cursor:
            ip = row[1]
            port = row[2]
            proxy_config = {'http': ip + ':' + port}
            proxy_handler = urllib2.ProxyHandler(proxy_config)
            openner = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(openner)
            #主要就是安装opener
            req = urllib2.Request(url, headers=self.header)
            content = urllib2.urlopen(req).read()
            print("Now content is :")
            print(content)
            time.sleep(200)

        conn.commit()
        conn.close()


    def getContent(self, url):
        req = urllib2.Request(url, self.header)
        resp = urllib2.urlopen(req)
        content = resp.read()
        return content

#标准的urllib2爬虫
def getPost(date_time, filter_p):
    url = 'https://zhhrb.sinaapp.com/index.php?date=' + date_time
    user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    header = {"User-Agent": user_agent}
    req = urllib2.Request(url, headers=header)
    resp = urllib2.urlopen(req)
    content = resp.read()
    p = re.compile('<h2 class="question-title">(.*)</h2></br></a>')
    result = re.findall(p, content)
    print(result)

#标准的urllib2爬虫
def get_page():
    user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    header = {"User-Agent": user_agent}
    #url="http://www.qq.com"
    url = "http://photo.xitek.com/style/0/p/1"
    req = urllib2.Request(url, headers=header)
    result = urllib2.urlopen(req).read()
    print(result)
    #p = re.compile(r'<a class='\blast\' href=\'/style/0/p/(\d+)' >')
    #p = re.compile('target="(.*)"')
    #p = re.compile('<img src="(.*?)" ')
    p = re.compile('<a class=\'blast\' href=\'/style/0/p/(\d+)\' >')
    #<a class='blast' href='/style/0/p/113' >
    page = p.findall(result)
    print(type(page))
    print(len(page))
    #print(page)
    '''
    if page:
        print(page[0])
        return page[0]
        # print(page[0])
        #return page[0]
    '''
    print("return")
    for i in page:
        print(i)

import urllib2,sys,StringIO,gzip,time,random,re,urllib,os
# 压缩内容解压
def getContentAuto(url):
        url=''
        headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM801 Build/LMY47V)'}
        req=urllib2.Request(url,headers=headers)
        resp=urllib2.urlopen(req)
        #time.sleep(2*random.random())
        content=resp.read()
        info=resp.info().get("Content-Encoding")
        if info==None:
            return content
        else:
            t=StringIO.StringIO(content)
            gziper=gzip.GzipFile(fileobj=t)
            html = gziper.read()
            return html

get_page()


#getPost('20160620',filter_p)
obj = Myurllib2()
#obj.proxy_test()
content = obj.getContent("http://xueqiu.com/8255849716")
print(content)

