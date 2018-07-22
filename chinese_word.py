# -*-coding=utf-8-*-
import requests
from lxml import etree
from bs4 import BeautifulSoup
import jieba.analyse

__author__ = 'Rocky'
'''
http://30daydo.com
Email: weigesysu@qq.com
'''
def get_content():
    url='https://www.jisilu.cn/question/280539'
    r = requests.get(url)
    r.encoding='utf-8'
    content = r.text

    # bs4
    total_content =[]
    bs=BeautifulSoup(content)
    for i in bs.find_all('div'):
        s=(str(i.string))
        # print(type(s))
        if s=='None':
            pass
        else:
            # print(s)
            total_content.append(s.strip())
    return ' '.join(total_content)
    # xpath
    # tree = etree.HTML(content)
    # words = tree.xpath('//div')
    # total_words = []
    # for w in words:
    #     total_words.append(w.xpath('string(.)').strip())
    # print(total_words)

def analysis():
    words = get_content()
    # print(words)
    ret =jieba.analyse.extract_tags(words,topK=20,withWeight=True,allowPOS=())
    # print(ret)
    for c,w in ret:
        print(c,w)
def main():
    # get_content()
    analysis()

if __name__ == '__main__':
    main()