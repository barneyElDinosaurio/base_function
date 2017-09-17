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


level_name = 'info'
level = LEVELS.get(level_name)
logging.basicConfig(level=level)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical error message')


