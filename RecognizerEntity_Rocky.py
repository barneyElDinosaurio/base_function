# -*- coding: utf-8 -*-
 
import codecs
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
 
#读取待处理文本
'''
    读取的文本格式是encoding参数值，codecs函数将其转化为unicode格式。
'''
news_files = codecs.open('news_content.txt','r',encoding='utf8')
news_list = news_files.readlines()
#type(news_list[1].encode('utf-8'))
 
 
#分句
'''
此函数参数输入的格式必须为str格式，所以直接获取的list里的参数值需要
通过encode('utf-8')，从Unicode转换为str
'''
def sentence_splitter(sentence):
    sents = SentenceSplitter.split(sentence)
    print('\n'.join(sents))
    sents_list = list(sents)
    return sents_list
    
 
#分词   
def segmentor(sentence):
    segmentor =  Segmentor()
    segmentor.load('E:\\git\\ltp-data-v3.3.1\\ltp_data\\cws.model')#加载模型
    words = segmentor.segment(sentence) #分词
    #默认可以这样输出
    #print '\t'.join(words)
    #可以转化成List输出
    word_list = list(words)
    segmentor.release()#释放模型
    return word_list 
 
#词性标注
def posttagger(words):
    postagger = Postagger()
    postagger.load('E:\\git\\ltp-data-v3.3.1\\ltp_datapos.model')
    posttags=postagger.postag(words)  #词性标注
    postags = list(posttags)
    postagger.release() #释放模型
    #print type(postags)
    return postags
 
#命名实体识别
def ner(words,postags):
    print('命名实体开始！')
    recognizer = NamedEntityRecognizer()
    recognizer.load('E:\\git\\ltp-data-v3.3.1\\ltp_data\\ner.model') #加载模型
    netags = recognizer.recognize(words,postags) #命名实体识别
    for word,ntag in zip(words,netags):
        print(word+'/'+ ntag)
    recognizer.release()   #释放模型
    nerttags = list(netags)
    return nerttags
 
#新建一个txt文件保存命名实体识别的结果    
out_file = codecs.open('out_nerfile.txt','w',encoding='utf8')
sents = sentence_splitter(news_list[1].encode('utf-8'))
for sent in sents:
    words=segmentor(sent)
    tags = posttagger(words)
    nertags = ner(words,tags)
    for word,nertag in zip(words,nertags):
        out_file.write(word.decode('utf-8')+'/'+nertag.decode('utf-8')+' ')
            
out_file.close()
