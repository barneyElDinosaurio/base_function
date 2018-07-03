# -*-coding=utf-8-*-
import pandas as pd
import json
import pymongo
from sqlalchemy import create_engine
client = pymongo.MongoClient('localhost')
doc = client['punish']['person']
engine = create_engine('mysql+pymysql://root:123456z@localhost/spider?charset=utf8')
temp=[]

for i in doc.find({}):
    del i['_id']
    temp.append(i)
df = pd.read_json(json.dumps(temp))
df.to_sql('tb_person_test',con=engine,if_exists='replace')