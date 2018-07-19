import hashlib
from setting import get_engine
import pandas as pd
import itertools
engine =get_engine('')
df= pd.read_sql('aws_users',engine,index_col='uid')
# print(df)

def is_same(x,y):
	return 1 if x==y else 0

def crash(salt,src):
	# salt='gzyl'
	m = hashlib.md5()   
	m.update(src)   
	first_md5 = m.hexdigest()
	m2 = hashlib.md5() 
	m2.update(first_md5+salt)
	final_md5 = m2.hexdigest()
	return final_md5

def loop_crash(src):
	df['src']=src
	df['new_pass']=map(crash,df['salt'],df['src'])
	df['result'] = df.apply(lambda x:is_same(x.password,x.new_pass),axis=1)
	if len(df[df['result']==1])>0:
		print(df[df['result']==1]['email'])
		print(src)

def start_crash():

	# for i in itertools.permutations('1234567890', 6):
	# 	x=''.join(i)
	# 	# print(x)
	# 	loop_crash(x)

	for i in range(0,1000000):
		src=str(i).zfill(6)
		print(src)
		loop_crash(src)

start_crash()