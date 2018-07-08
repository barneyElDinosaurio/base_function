# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
#排序
from itertools import permutations
a=['a','b','c','d']
for i in permutations(a,2):
    print(i[0],i[1])


