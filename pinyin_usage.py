# -*-coding=utf-8-*-

# @Time : 2018/10/10 9:22
# @File : pinyin_usage.py
from pypinyin import lazy_pinyin,Style

def change_pinyin(name):
    ret =lazy_pinyin(name,errors='ignore')
    short_cut = lazy_pinyin(name, style=Style.FIRST_LETTER)

    result = ret[:1]+short_cut[1:]
    # 返回不同组合的名字
    return ''.join(ret),'_'.join(ret),'_'.join(ret[:2])+''.join(ret[2:]),''.join(result),'_'.join(result[:2])+''.join(result[2:])


name = '刘备哥'
print(change_pinyin(name))
# print(change_pinyin_first(name))