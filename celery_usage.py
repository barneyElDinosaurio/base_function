# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
from celery import Celery
ip='10.19.133.255'
broker='redis://%s:7777/5'
backend='redis://%s:7777/6'

app=Celery('celery_usage',broker=broker,backend=backend)

@app.celery_usage
def add(x,y):
    return x+y