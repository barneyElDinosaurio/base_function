# -*- coding:utf-8 -*-
import sys
import urllib
#reload(sys)
#sys.setdefaultencoding('utf-8')
import chardet


def chinese_str():
    w = open("C:\Kingsoft\Python\q.txt", "a")
    for i in range(1, 100):
        print(str(i))
        w.write(str(i) + "\n")
        # w.write(u"程先生")
    w.close()

# print u"程先生"

'''
name=u"程先生"
if isinstance(name,unicode):
	print "unicode"
	print name
else:
	print "non unicode"
	print name
print sys.getdefaultencoding()
'''
#f=open('b.txt','a',encoding='utf-8')
#name=u"陈先生"
#f.write(name)
#f.close()
#print "Done"


def check_year():
    year = 11
    if isinstance(year, str):
        print "Bingo"


def _write_adead():
    sys.stdout.write("Helloafafdafafafafd\n")
    print sys.version_info[0]


def zfill_test():
    temp = "Rocky Chen"
    temp = temp.zfill(20)
    print temp

    print len(temp)
    f = lambda x: str(x).zfill(6)
    a = f(234)
    print a
    print type(a)


def loo_each():
    str1 = "You are bitch!\n"
    print str1
    word = [x.strip() for x in str1.split(' ')]
    print word
    conn = " ".join(word)
    print conn
    if 'bitch' in str1:
        print "Bitch"


def replace_func():
    a = ' i love this game . I hate this game, no love '
    print a,
    print 'end'
    print a.lstrip(),
    print 'end'
    b = 2
    c = 3
    print b, c
    print a,
    print 'end'


def garbe_character():
    print "\x00"


def slic():
    code = '002341'
    print code[:1]

def replace_test():
    a='s gsz'
    if ' ' in a:
        a=a.replace(' ','')
    print a

def split_fun():
    l="This is a test string from Andrew".split()
    print l
    link='http://quotes.toscrape.com/page/1/'
    l_link=link.split('/')
    print l_link


    a='https://shenzhen.anjuke.com/community/p50/'
    b='https://shenzhen.anjuke.com'
    x=a.split(b)
    print x
def url_encode():
   w='欧陆经典'

   #s1=unicode(w,"gbk")
   x=urllib.quote(w)
   print x
   print chardet.detect(w)

def format_case():
    now4='201777777'
    #url = 'https://api.anjuke.com/mobile/v5/community/list\?page_size=25&area_id=0&city_id=13&page=1&lat=22.565992&block_id=0&lng=113.953578&androidid=4dd00e258bbe295f&uuid=26f709cf-699c-4aa4-9563-019ed46e713e&cid=-1&pm=b638&version_code=321813&m=Android-SM801&qtime=%s&from=mobile&app=a-ajk&v=5.1.1&i=990006203070023&_pid=15964&cv=10.10.2&o=icesky_msm8992-user\%205.1.1\%20LMY47V\%201\%20release-keys&macid=12a0fc64a12e5d8a1ef367d0bccb9690&_chat_id=0&manufacturer=smartisan HTTP/1.1' %now4
    url='dd//&dd%%20%s' %now4
    print url
    id='123456'
    city='dg'
    page='1'
    req_url = 'https://m.fang.com/zf/?projcodes={}&src=xiaoqu&jhtype=zf&renttype=cz&c=zf&a=ajaxGetList&city={}&page={}'
    req_url = req_url.format(id,city,page)

    print req_url
def show_data():
    x={"status": "20001", "msg": "\u7b7e\u540d\u9519\u8bef"}
    for k,v in x.items():
        print k,v

    j= x['msg'].split('\\')
    for i in j:
        print i.decode('utf-8')
    str1=''

def testNone():
    x=None
    if x is not None:
        print "Go"

    else:
        print "None"

def type_compare():
    x=[1,2,3,4]

    if x==404:
        print "error"
    else:
        print 'bingo'

def cityLink():
    url='http://bj.fang.com/'
    url2='http://bj.fang.com'
    x1=url.split('/')[-1]
    print len(x1)
    x2=url2.split('/')[-1]
    print len(x2)
    url3='https://m.lianjia.com/cd/xiaoqu'
    x3=url3.split('/')
    print x3

def code_case():
    s = "人生苦短"
    s1 = u"人生苦短"
    s2 = unicode("人生苦短", "utf-8")

    su = "人生苦短"
    u = s.decode("utf-8")
    sg = u.encode("gbk")
    print sg
    print type(s)
    print type(s1)
    print type(s2)
    print type(su)
    print type(u)
    print type(sg)
    print s.encode('gbk')

def check_default_type():
    a=u'上海'
    print a
    print type(a)
    b=a.encode('unicode-escape').decode('string_escape')
    print b.encode('gb2312')
    print type(b)
    print b
    c=a.encode('utf-8')
    print c
    print type(c)
    d=u'\xbd\xa8\xd6\xfe\xc0\xe0\xd0\xcd\xa3\xba'
    print unicode(d)

def len_case():
    a=''
    print len(a)

def geturlid():
    url='http://m.qfang.com/taicang/garden'
    url_list = url.split('/')
    houseid = url_list[-1]
    url_list[len(url_list)-1]='rent'
    url_list.append(houseid)
    url ='/'.join(url_list)
    / taicang


#check_year()
#_write_adead()
#zfill_test()
#loo_each()
#replace_func()
#garbe_character()
#slic()
#replace_test()
#split_fun()
#url_encode()
#format_case()
#show_data()
#testNone()
#type_compare()
#cityLink()
#code_case()
#check_default_type()
#len_case()
geturlid()