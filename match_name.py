# coding: utf-8
import pandas as pd
import json
from difflib import SequenceMatcher,Differ
pd.set_option('display.max_rows',None)
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
    #return Differ(None, a, b).ratio()

sz_df=pd.read_csv('shenzhen.csv')
name='百花'
result = pd.DataFrame(columns=['city_name', 'location', 'name', 'score', 'spider'])
#for name in df2.name:
result_1 = sz_df
result_1['score'] = map(lambda x: similar(name, x), result_1['name'])
result_1['spider'] = name
result_1 = result_1.sort_values('score', ascending=False)
# 匹配度排名
highest = result_1[:3]
#print(result_1)
#
print(highest)
ll= list(highest['price'].values)
print(json.loads(ll[0])['2017-07'][0]['price'])

#result = result.append(highest)