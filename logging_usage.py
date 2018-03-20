# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''

import logging,sys
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

def case1():
	level_name = 'info'
	level = LEVELS.get(level_name)
	logging.basicConfig(level=level)

	logging.debug('This is a debug message')
	logging.info('This is an info message')
	logging.warning('This is a warning message')
	logging.error('This is an error message')
	logging.critical('This is a critical error message')

def case2():
	
	logger =logging.getLogger('mylogger')
	logger.setLevel(logging.DEBUG)

	f_handler = logging.FileHandler('logging.log')
	f_handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')

	f_handler.setFormatter(formatter)	
	logger.addHandler(f_handler)

	logger.debug('debug foobar 2')


def main():
	case2()

if __name__=='__main__':
	main()

