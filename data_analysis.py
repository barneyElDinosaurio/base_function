#-*-coding=utf-8-*-
import os
import pandas as pd
import numpy as np
import datetime


def base_usage():
	filename='600609.xls'
	df = pd.read_excel(filename)
	
	print 'df info: ',df.info()
	print 'df describe' , df.describe()
	print 'df index', df.index
	print df.head(10)

	df_new_index =  df.set_index(pd.Series(np.arange(len(df))*2))

	print df_new_index

	print df.open
	print type(df.open)
	print type(df['open'])
	print type(df[['code','open']])
	print df[:10]
	df_set_index = df.set_index(df['datetime'])
	print df_set_index.head(10)
	del df_set_index['datetime']
	print 'df head 15',df_set_index.head(15)
	print df_set_index[:10]
	print 'df : usage ',df_set_index[:'2017-12-11']
	print 'df ix',df_set_index.ix['2017-12-11']
	print 'slice : ', df_set_index.ix[5:7:,2:6:]
	print 'slice : ', df_set_index.ix['2017-12-01':'2017-10-01':,2:6:]
	print 'df iloc & loc',df_set_index.iloc[[1,2,3],[1,6]]
	print 'df iloc & loc',df_set_index.iloc[1:7,2:6]
	print df_set_index.info()
	print 'df iloc & loc',df_set_index.iloc[1:7,2:6]
	print 'df iloc & loc',df_set_index.loc[[datetime.datetime(2017,12,22)],['open']]


	print 'change colums order'
	new_df = pd.DataFrame(df_set_index,columns=['vol','code'],index=[datetime.datetime(2017,12,01)])
	new_df1 = pd.DataFrame(df_set_index,columns=['vol','code','name'],index=[datetime.datetime(2017,12,01),datetime.datetime(2017,12,22)])
	print new_df1
	new_df1['name']='Rocky'
	print new_df1
	new_df1.rename(columns={'name':'Name'},inplace=True)
	print new_df1
	new_df1['score']=np.random.randn(len(new_df1))
	print new_df1
	fixed=pd.Series(['Shawn','Joe'],index=[datetime.datetime(2017,12,01),datetime.datetime(2017,12,22)])
	new_df1['Name']=fixed
	print 'after change by series',new_df1

	new_df1['sex']='f'
	print 'set sex',new_df1
	new_df1.drop(datetime.datetime(2017,12,01),axis=0,inplace=True)
	print 'after drop',new_df1

	print 'sorting'
	print df.sort_index(ascending=False)

	new_df1.index=[1]
	print new_df1
	print df.sort_index(axis=1)
	print 'order by close price\n',df.sort_values(by='close',ascending=False)


	print '*'*20
	print '\n'
	rrk=pd.Series([10,12,9,9,14,4,2,4,9,1])
	print rrk
	print 'sorting series'
	print rrk.sort_values()
	print rrk.rank(method='max')
	new_df2=(df_set_index['high']+df_set_index['low'])/2
	print 'cal df \n',new_df2

def calc():
	df1=pd.DataFrame(np.random.randint(10,size=10).reshape(2,5),columns=list('bcaed'))
	print df1

	df2= pd.DataFrame(np.random.randint(10,size=12).reshape(3,4),columns=list('abcd'))
	print df2
	rangef=lambda x:x.max()-x.min()

	df3 = df1.add(df2,fill_value=0)
	print df3

	print rangef(df3)
	print df3.apply(rangef,axis=0)
	print df3.apply(rangef,axis=1)

	print 'df count()\n',df1.count()

	high_change = lambda x:x-1
	filename='600050.xls'
	df = pd.read_excel(filename)
	print df.head(5)
	df=df.set_index('datetime')
	print 'after set index\n',df.head(10)
	df['high']=df['high'].map(high_change)
	print 'after map\n',df.head(10)

	df['color'] = map(lambda x:'red' if x>0 else 'none' if x==0 else 'greed',df['close']-df['open'])
	print df.head(20)
	print 'value_counts\n',df['color'].value_counts()
	df_group = df.groupby(df['color'])
	print 'group \n',df_group
	print 'groupby describle \n',df_group.describe()


def main():
	# base_usage()
	calc()

if __name__=='__main__':
	data_path=os.path.join(os.getcwd(),'data')
	os.chdir(data_path)	
	main()

