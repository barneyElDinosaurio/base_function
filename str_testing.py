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
#check_year()
#_write_adead()
#zfill_test()
#loo_each()
#replace_func()
#garbe_character()
#slic()
#replace_test()
split_fun()
#url_encode()