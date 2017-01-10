# -*-coding=utf-8-*-
import re
__author__ = 'Rocky'
org_str=u"我是一名中国人<br>吗</br>？Helo<br>World</br>"
print org_str
dest_str=re.sub('<br>|</br>','\n',org_str)
print dest_str
