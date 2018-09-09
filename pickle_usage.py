# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
try:
    import cPickle as pickle
except:
    import pickle

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
        for i in p:
            print(i*3)

write_file()
read_file()
