#-*-coding=utf-8-*-

def case1():
	from sklearn import datasets
	news = datasets.fetch_20newsgroups(subset='all')
	# print len(news.data)
	# print len(news.target)

	# print '*'*10
	# print news.data[0]
	# print '*'*10
	# print news.target[0]
	from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
	vec = CountVectorizer()
	x = vec.fit_transform(news.data)
	# print x.shape
	# print x[:2]
	print x[:10,:10].toarray()
	TFIDF = TfidfTransformer()
	x_tfidf = TFIDF.fit_transform(x)
	print x_tfidf[:10,:10].toarray()


	from sklearn.cross_validation import train_test_split
	Xtrain, Xtest, ytrain,ytest =train_test_split(x,news.target,test_size = 0.3,random_state=233)

	tf_Xtrain, tf_Xtest, tf_ytrain,tf_ytest =train_test_split(x_tfidf,news.target,test_size = 0.3,random_state=233)


	from sklearn.naive_bayes import MultinomialNB
	mnb =MultinomialNB()
	tf_mnb = MultinomialNB()

	mmb.fit(Xtrain,ytrain)
	tf_mnb.fit(tf_Xtrain,tf_ytrain)


def case2():
	from sklearn.datasets import make_classification

	x,y = make_classification(n_samples=1000, n_features=2,n_redundant=0,n_informative=1,n_clusters_per_class=1)

	print len(x)
	print len(y)
	print x
	print y
	for i in range(len(x)):
		print x[i],y[i]

	x_data_train = x[:800,:]

	x_data_test = x[800:,:]
	y_data_train = y[:800]
	y_data_test = y[800:]

	print '*'*20
	print x_data_train
	print x_data_test
	print y_data_train
	print y_data_test

	print x[0,0]


def case3():
	#导入pandas与numpy工具包
	import pandas as pd
	import numpy as np
	#创建特征名称列表
	columns_names=['Sample code number','Clump Thickness','Uniformity of Cell Size',
	               'Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size',
	               'Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']
	#使用pandas.read_csv函数从互联网读取指定数据
	data=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',
	                 names=columns_names)
	#将'?'替换为标准缺失值表示
	data=data.replace(to_replace='?',value=np.nan)
	#丢弃带有缺失值的数据（只要一个维度有缺失值）
	data=data.dropna(how='any')
	#输出data的数据量和维度
	print data.shape
	#(683,11)
	print data

# case2()
case3()