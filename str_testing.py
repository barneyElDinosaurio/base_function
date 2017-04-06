# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def chinese_str():
    w=open("C:\Kingsoft\Python\q.txt","a")
    for i in range(1,100):
        print(str(i))
        w.write(str(i)+"\n")
        #w.write(u"程先生")
    w.close()

#print u"程先生"

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
    year=11
    if isinstance(year,str) :
        print "Bingo"

def _write_adead():
    sys.stdout.write("Helloafafdafafafafd\n")
    print sys.version_info[0]

def zfill_test():
    temp="Rocky Chen"
    temp=temp.zfill(20)
    print temp

    print len(temp)
    f=lambda x:str(x).zfill(6)
    a=f(234)
    print a
    print type(a)

def loo_each():
    str1="You are bitch!\n"
    print str1
    word=[x.strip() for x in str1.split(' ')]
    print word
    conn=" ".join(word)
    print conn
    if 'bitch' in str1:
        print "Bitch"

def replace_func():
    a=' i love this game . I hate this game, no love '
    print a,
    print 'end'
    print a.lstrip(),
    print 'end'
    b=2
    c=3
    print b,c
    print a,
    print 'end'



#check_year()
#_write_adead()
#zfill_test()
#loo_each()
replace_func()