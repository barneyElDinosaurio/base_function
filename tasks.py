# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
from celery import Celery
ip='10.19.133.255'
broker='redis://%s:7777/5' %ip
backend='redis://%s:7777/6' %ip

app=Celery('tasks',broker=broker,backend=backend)

@app.tasks
def add(x,y):
    return x+y