# -*-coding=utf-8-*-
import re
__author__ = 'Rocky'
def case1():
    org_str = u"我是一名中国人<br>吗</br>？Helo<br>World</br>"
    print(org_str)
    dest_str = re.sub('<br>|</br>', '\n', org_str)
    print(dest_str)

    t1='i love baseketball 13424281084!'
    #phone_number=re.search

    text = 'c++ python2 python3 perl ruby lua javascript java php4 php5 c'
    print(re.match(r'java',text))
    print(re.search(r'java',text).group())

    line='RockFish 55'
    name2 = re.findall('^(.+)\s+\d+', line)
    print(name2)

    print('\n'*5)
    s='?orgame=1&categoryId=-10'
    print(s)
    p=re.compile('categoryId=(-?\d+)')
    x=p.findall(s)
    print(x)
    kw0='萧宏·普罗旺斯'
    print(kw0)
    kw_p=re.findall('·',kw0)
    print(kw_p)

    ip='112.95.16.107'
    if re.match('\.',ip) is None:
        print("can't get IP")
    else:
        print("IP: ",ip)

def latitude():
    ss='province=dd;city=dd;tttt=woaini'
    p=re.compile('tttt=(.*)')
    rt=p.findall(ss,re.S)
    print(len(rt))
    print(rt[0])

def book():
    s= 'I am python modules test for re modules, I am'
    print(re.search('am',s))
    print(re.search('am',s).group())
    print(re.match('am',s))
    print(re.match('I am',s))
    print(re.findall('modul.*',s))
    print(re.finditer('modules',s))



# latitude()
book()