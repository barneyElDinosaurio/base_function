# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''

import pyautogui as pag
import datetime
def ready_rest():
	f= open('notice.txt','a')
	ret = pag.prompt(u"有任务去做，马上！")
	if ret =='go':
		f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		f.write('\t')
		f.write('Go to do now')
		f.write('\n')
	else:
		f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		f.write('\t')
		f.write('Failed to to to do !')
		f.write('\n')
	f.close()

ready_rest()