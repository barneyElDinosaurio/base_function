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
type_compare()
