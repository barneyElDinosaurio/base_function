# coding: utf-8
import codecs
import json
import subprocess
import time

'''
fp = codecs.open('anjuke_city','r')
str_data = fp.read()
js = json.loads(str_data)
'''
# std_fp = open('spider1.log', 'a')
# err_fp = open('spider_err1.log', 'a')
'''
for k, v in js.items():

    cmd = 'scrapy crawl anjuke_m -a city=%s' % k
    print(cmd)
    p = subprocess.Popen(cmd, stdout=std_fp, stderr=err_fp, shell=True)
    p.communicate()
    p.wait()
    time.sleep(120)
'''

fp2 = open('anjuke_rent.txt', 'r')

# city_chinese_name = fp2.readlines()
# city_chinese_name=map(lambda x:x.strip(),city_chinese_name)
city_chinese_name = []
while 1:
    s = fp2.readline()
    if len(s) != 0:
        city_chinese_name.append(s.strip())
    else:
        break
'''
for city in city_chinese_name:
    #print(city_chinese_name)
    print(len(city_chinese_name))

    cmd = 'scrapy crawl anjuke_rent -a city=%s' %city.strip()
    print(cmd)
    p = subprocess.Popen(cmd, stdout=std_fp, stderr=err_fp, shell=True)
    p.communicate()
    p.wait()

    city_chinese_name.remove(city)
    #time.sleep(10)
print(city_chinese_name)
'''
# for i in city_chinese_name:
# print(i)
# print('end')
l = len(city_chinese_name)
i = l - 1
print('len of : ', l)
while i > -1:
    print(city_chinese_name[i])
    del city_chinese_name[i]
    i = i - 1
    print(len(city_chinese_name))

print('last')
print(city_chinese_name)
print(len(city_chinese_name))
# fp2.close()
# std_fp.close()
# err_fp.close()
'''
cmd = 'scrapy crawl anjuke_rent -a city="东莞"'
print(cmd)
p = subprocess.Popen(cmd, stdout=std_fp, stderr=err_fp, shell=True)
p.communicate()
p.wait()
'''