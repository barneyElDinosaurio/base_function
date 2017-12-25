#-*-coding=utf-8-*-
import os,time
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy import stats
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


def time_item():
	print pd.Timestamp('now')
	dates=pd.date_range('2017-01-01','2017-02-01')
	print dates
	s1= pd.Series(np.random.randn(len(dates)),index=dates)
	f1= pd.DataFrame(np.random.randn(len(dates)),index=dates)
	print 's1\n',s1
	print 'f1\n',f1
	filename='600050.xls'
	df = pd.read_excel(filename)
	print 'df info\n',df.info()
	df=df.set_index('datetime')
	print 'df \n',df.head(20)
	print 'Nov data\n',df['2017-11']
	print 'truncate \n',df.truncate(after='2017-10-01')
	s3=df['close'].truncate(after='2017-10-01')
	fig=plt.figure()
	s3.plot()
	plt.show()

def missing_value():
	d={
	'name':['Allen','Ben','Cindy','Danny'],
	'age':[21,22,43,22],
	'sex':['f','f','m','f']}
	df = pd.DataFrame(d)
	print df
	df.iloc[[1,2],[1]]=[np.nan,np.nan]
	print df
	df=df.fillna(method='ffill')
	print 'after fill\n',df
	df.loc[[2],['sex']]=[np.nan]
	print 'change sex\n',df
	print df.dropna(axis=0)
	# print 'after drop\n',df
	print df.dropna(how='all',axis=1)
	df['number']=np.arange(len(df))
	df.loc[2,'number']=np.nan
	print df
	print df.interpolate(method='values')

def statistice_case():

	df=pd.DataFrame()
	df['age']=np.arange(1,11)
	df['score']=np.arange(10,30,2)
	print df
	print 'mean\n',df['age'].mean()
	print 'mean\n',df['score'].mean()
	print 'mean\n',df.mean()

	print 't mean\n',stats.tmean(df['age'],[2,10])

	print 'median\n',df['age'].median()
	print 'median\n',df['score'].median()
	print 'quarttile \n',stats.scoreatpercentile(df['age'],[25,50,75,100])
	df['count']=[1,2,3,4,5,6,7,8,8,8]
	print 'mode \n',df['count'].mode()

def stock_analysis():
	filename=datetime.datetime.now().strftime('%Y-%m-%d')+'.xls'
	stock_df = pd.read_excel(filename)
	
	# change amount to xxx W
	stock_df['amount']=map(lambda x:round(x*1.0/10000,1),stock_df['amount'])
	# print stock_df.head(10)
	# time.sleep(20)
	print 'count \n',stock_df['changepercent'].count()
	print 'median \n',stock_df['changepercent'].median()
	print '0% count \n',stock_df[stock_df['changepercent']==0]['code'].count()
	print '0% name \n',stock_df[stock_df['changepercent']==0][['code','name','changepercent']]
	print 'percentile\n',stats.scoreatpercentile(stock_df['changepercent'],[25,50,75])
	print 'percentile\n',stats.scoreatpercentile(stock_df['amount'],[25,50,75])
	print 'median\n',stock_df['amount'].median()
	print 'mean\n',stock_df['amount'].mean()
	# stock_df['amount'].plot()
	# plt.show()

	zglt_df = pd.read_excel('600050.xls')
	print zglt_df.head(20)
	print 'corr \n',zglt_df['amount'].corr(zglt_df['vol'])
	print 'corr \n',zglt_df['vol'].corr(zglt_df['close'])
	print 'max\n',zglt_df['high'].max()
	print 'location of max\n',zglt_df.loc[zglt_df['high'].idxmax(),::]
	print 'max\n',zglt_df['high'].min()
	print 'location of min\n',zglt_df.loc[zglt_df['high'].idxmin(),::]

	print 'change date to calc\n'
	zglt_df_t = zglt_df.set_index('datetime')
	print zglt_df_t.head(10)
	print zglt_df_t.info()
	zglt_df_2017=zglt_df_t.truncate(after='2017-01-01')
	print zglt_df_2017.tail(10)
	print 'max\n',zglt_df_2017['high'].max()
	print zglt_df_2017['high'].idxmax()
	print 'location of max\n',zglt_df_2017.loc[zglt_df_2017['high'].idxmax()]
	print 'max\n',zglt_df_2017['high'].min()
	print zglt_df_2017['high'].idxmin()
	print 'location of min\n',zglt_df_2017.loc[zglt_df_2017['high'].idxmin()]




def main():
	# base_usage()
	# calc()
	# time_item()
	# missing_value()
	# statistice_case()
	stock_analysis()
if __name__=='__main__':
	data_path=os.path.join(os.getcwd(),'data')
	os.chdir(data_path)	
	main()

