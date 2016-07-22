import time,datetime

now = time.strftime("%Y-%m-%d")
print now
print type(now)
now_time = datetime.datetime.now()
print now_time
print type(now_time)
today = time.strftime("_%Y_%m_%d")
print today