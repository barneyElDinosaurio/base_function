# coding: utf-8
import re
fp=open('city.txt','r').read()
#print fp
s=re.sub(r'/\* \d+ \*/','',fp)
#dic=eval(s)
print s
s1=re.findall('"_id" : "(.*?)"',s)
s2=re.findall('"count" : (\d+)',s)

for i in range(len(s1)):
    print s1[i], " ", s2[i]

'''
ss=0
for i in s2:
    ss=ss+int(i)
    #print type(i)
'''
#print ss