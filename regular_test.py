# -*-coding=utf-8-*-
import re

__author__ = 'Rocky'
org_str = u"我是一名中国人<br>吗</br>？Helo<br>World</br>"
print org_str
dest_str = re.sub('<br>|</br>', '\n', org_str)
print dest_str

t1='i love baseketball 13424281084!'
#phone_number=re.search

text = 'c++ python2 python3 perl ruby lua javascript java php4 php5 c'
print re.match(r'java',text)
print re.search(r'java',text).group()

line='RockFish 55'
name2 = re.findall('^(.+)\s+\d+', line)
print name2

print '\n'*5
s='?orgame=1&categoryId=-10'
print s
p=re.compile('categoryId=(-?\d+)')
x=p.findall(s)
print x