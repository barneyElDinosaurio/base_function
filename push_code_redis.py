import redis
import tushare as ts

r = redis.StrictRedis('127.0.0.1',decode_responses=False)
df = ts.get_stock_basics()
print(df.head())
code_list = list(df.index.values)
r.lpush('code',code_list)