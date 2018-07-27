# -*-coding=utf-8-*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import codecs

<<<<<<< HEAD
filename = 'html.txt'
sentences = LineSentence(filename)
model = Word2Vec(sentences,size=128,window=5,min_count=5,workers=4)
model.save('word_embedding_128')

items = model.most_similar('中国')
for item in items:
	print(item[0],item[1])


print(model.similarity('男人','女人'))
=======
filename = 'wikizhword.text'
f = codecs.open(filename, 'r', encoding='utf-8')
line = 20
for _ in range(line):
    print(f.readline())
# sentences = LineSentence(f)
# model = Word2Vec(sentences,size=128,window=5,min_count=5,workers=4)
# model.save('word_embedding_128')
#
# #model=Word2Evc.load('word_embedding_128')
# items = model.most_similar('中国')
# for item in items:
# 	print(item[0],item[1])
#
#
# print(model.similarity('男人','女人'))
>>>>>>> origin/master
