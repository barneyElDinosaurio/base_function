# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import cPickle as pickle
import pprint
#import pickle,pprint
def write_file():
    obj=range(10)
    with open('save.pkl','wb') as f:
        pickle.dump(obj,f)


def read_file():
    with open('save.pkl','rb') as f:
        p=pickle.load(f)
        pprint.pprint(p)

write_file()
read_file()
