#-*-coding=utf-8-*-
import random

keys=[chr(i) for i in range(ord('A'),ord('Z')+1)]

print keys

values=[random.randint(0,100) for i in range(len(keys))]

print values

d=zip(keys,values)
print d
print type(d)
d1=dict(d)
print d1

k=sorted(d1.items(),key=lambda x:x[1],reverse=True)
print k

CUSTOMER_FROM_NAMES = (
    (1, u"无"),
    (2, u"首页登记"),
    (3, u"客服QQ"),
    (4, u"邮件"),
    (5, u"市场活动"),
    (6, u"电话咨询"),
    (7, u"电话外呼"),
    (8, u"商务扩展"),
    (9, u"内部推荐"),
    (10, u"公司分配"),
)

l=CUSTOMER_FROM_NAMES
l2= l[1:9]
l3=l2+l[:1]
print l3
print type(l[0])
print type(l[:1])
print l[0]
print l[:1]

print "*"*10
def sort_usge():
    dic={'a':33,'b':2,'c':44,'z':22,'d':89,'e':5}
    print dic
    for k,v in dic.items():
        print k,v
    dic2 = sorted(dic.iteritems(),key=lambda asd:asd[0],reverse=True)
    print dic
    print dic2

sort_usge()