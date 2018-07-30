# -*-coding=utf-8-*-
# @Time : 2018/7/30 16:23
# @File : pyltp_demo.py

from pyltp import Segmentor
import codecs
import re, os

LTP_DATA_DIR = 'E:\\git\\ltp-data-v3.3.1\\ltp_data'  # ltp模型目录的路径
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
sg_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 命名实体识别模型路径，模型名称为`pos.model`
pr_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 命名实体识别模型路径，模型名称为`pos.model`
ps_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 命名实体识别模型路径，模型名称为`pos.model`


# ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`


def cut_word():
    with codecs.open('html.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    # print(content)
    # content='元芳你怎么看？我就趴窗口上看呗！'
    p = re.compile('\s', re.S)
    content = p.sub('', content)
    segmentor = Segmentor()
    segmentor.load("E:\\git\\ltp-data-v3.3.1\\ltp_data\cws.model")

    words = segmentor.segment(content)
    print("|".join(words))
    segmentor.release()


def name_recognize():
    import os

    from pyltp import NamedEntityRecognizer
    recognizer = NamedEntityRecognizer()  # 初始化实例
    recognizer.load(ner_model_path)  # 加载模型

    words = ['元芳', '你', '怎么', '看']
    postags = ['nh', 'nh', 'nh', 'nh']
    netags = recognizer.recognize(words, postags)  # 命名实体识别

    print('\t'.join(netags))
    recognizer.release()  # 释放模型


def name_recognize_one():
    import sys, os
    import pyltp
    from pyltp import SentenceSplitter, Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

    paragraph = '叙利亚东古塔地区。7日发生疑似化学武器袭击事件，导致70余人丧生。报道一出，叙利亚反对派、美国、英国、法国等纷纷指责叙政府军使用化学武器袭击无辜平民。但叙利亚坚决否认，并指责西方和叙反对派造谣，目的是保护被围困的恐怖分子。俄外交部则认为，该谣言旨在袒护恐怖分子，并为外部势力发动打击寻找借口。'

    sentence = SentenceSplitter.split(paragraph)[1]
    print('split {}'.format(sentence))
    # 断句
    #     for i in sentence:
    #         print(i)
    #         print()
    segmentor = Segmentor()
    segmentor.load(sg_model_path)
    words = segmentor.segment(sentence)
    print('|'.join(words))

    postagger = Postagger()
    postagger.load(ps_model_path)
    postags = postagger.postag(words)
    for k, v in dict(zip(words, postags)).items():
        print(k, v)

    # print(' ## '.join(postags))
    parser = Parser()
    parser.load(pr_model_path)
    arcs = parser.parse(words, postags)
    print(' '.join('%d:%s ' % (arc.head, arc.relation) for arc in arcs))

    print('#' * 8)
    recognizer = NamedEntityRecognizer()
    recognizer.load(ner_model_path)
    netag = recognizer.recognize(words, postags)
    for word, ntag in zip(words, netag):
        if ntag != 'O':
            # print('ntag')
            print(word + ' / ' + netag)
    print(' / '.join(netag))

    # 命名实体识别
    word_list = ['欧几里得', '是', '西元前', '三', '世纪', '的', '希腊', '数学家', '。']
    postags_list = ['nh', 'v', 'nt', 'm', 'n', 'u', 'ns', 'n', 'wp']
    nertags = recognizer.recognize(word_list, postags_list)
    for word,ntag in zip(word_list, nertags):
        if ntag != 'O':
            print(word + '/' + ntag)
    #print (" ".join(word_list))
    print (' '.join(nertags))

    segmentor.release()
    postagger.release()
    parser.release()
    recognizer.release()


def official_demo():
    import sys
    ROOTDIR = 'E:/git/ltp-data-v3.3.1/'
    # sys.path = [os.path.join(ROOTDIR, "lib")] + sys.path

    # Set your own model path
    MODELDIR = os.path.join(ROOTDIR, "./ltp_data")

    from pyltp import SentenceSplitter, Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

    paragraph = '中国进出口银行与中国银行加强合作。中国进出口银行与中国银行加强合作！'

    sentence = SentenceSplitter.split(paragraph)[0]

    segmentor = Segmentor()
    segmentor.load(os.path.join(MODELDIR, "cws.model"))
    words = segmentor.segment(sentence)
    print("\t".join(words))

    postagger = Postagger()
    postagger.load(os.path.join(MODELDIR, "pos.model"))
    postags = postagger.postag(words)
    # list-of-string parameter is support in 0.1.5
    # postags = postagger.postag(["中国","进出口","银行","与","中国银行","加强","合作"])
    print("\t\t".join(postags))

    parser = Parser()
    parser.load(os.path.join(MODELDIR, "parser.model"))
    arcs = parser.parse(words, postags)

    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))

    recognizer = NamedEntityRecognizer()
    recognizer.load(os.path.join(MODELDIR, "ner.model"))
    netags = recognizer.recognize(words, postags)
    print("\t".join(netags))


def demo_three():
    string = '这个把手该换了，我不喜欢日本和服，别把手放在我的肩膀上，工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作'
    segmentor = Segmentor()
    segmentor.load(sg_model_path)
    ret =segmentor.segment(string)
    print('/'.join(ret))
    segmentor.release()
    # print(result)
# name_recognize_one()
# official_demo()
demo_three()