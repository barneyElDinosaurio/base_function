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
check_year()
_write_adead()

