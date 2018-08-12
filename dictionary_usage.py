# -*-coding=utf-8-*-
import random


def base_usage():
    keys = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    print(keys)

    values = [random.randint(0, 100) for i in range(len(keys))]

    print(values)

    d = zip(keys, values)
    print(d)
    print(type(d))
    d1 = dict(d)
    print(d1)

    k = sorted(d1.items(), key=lambda x: x[1], reverse=True)
    print(k)


def choice_usage():
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

    l = CUSTOMER_FROM_NAMES
    l2 = l[1:9]
    l3 = l2 + l[:1]
    print(l3)
    print(type(l[0]))
    print(type(l[:1]))
    print(l[0])
    print(l[:1])


# 字典按照键或者值来排序
def sort_usge():
    dic = {'a': 33, 'b': 2, 'c': 44, 'z': 22, 'd': 89, 'e': 5}
    print(dic)
    for k, v in dic.items():
        print(k, v)
    dic2 = sorted(dic.iteritems(), key=lambda asd: asd[0], reverse=True)
    print(dic)
    print(dic2)
    dic3 = sorted(dic.keys())
    print(dic3)


# 根据值来找键
def find_key():
    # 创建一个随机的字典
    keys = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    vals = [random.randint(1, 100) for _ in range(len(keys))]
    d = dict(zip(keys, vals))

    print(d)
    p = 55
    for k, v in d.items():
        if p == v:
            print(k)
            break

def dict_create():
    a=[('a',1),('b',2)]
    b=dict(a)
    print(b)
    c={}.fromkeys([i for i in range(10)])
    print(c)
    d=c.keys()
    print(d)

class SortDict(dict):
    def keys(self):
        return sorted(super(SortDict,self).keys())

def sort_test():
    d = SortDict({'a': 33, 'b': 2, 'c': 44, 'z': 22, 'd': 89, 'e': 5})
    d1 = SortDict((('zheng-cai',67),('hui-jun',11),('xin-yi',88)))
    print(d.keys())
    print(d1.keys())

def multi_dictionary():
    user=dict()
    print(user)
    user['Dave']={"Rocket":2}
    print(user)

def dict_update():
    a={'A':1,'B':2,'C':3}
    print(a)
    a.update({'A':9,'D':10})
    print('new a : {}'.format(a))

def full_run():
    import sys
    top = 4*44739243
    f={}
    try:
        for k in range(0, top):
            sys.stdout.write('%d %f%%\r' % (k, k * 100.0 / top))
            f[k]=k
    except:
        print()
        print("limit:")
        print(k)
        raise

def main():
    #sort_usge()
    # base_usage()
    #find_key()
    #dict_create()
    # sort_test()
    # multi_dictionary()
    # dict_update()
    full_run()

if __name__ == '__main__':
    main()