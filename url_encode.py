# coding: utf-8
import urllib
queryStr='news'
new_str=queryStr.encode('utf-8')
encodedStr = urllib.quote(new_str)
#encodedStr = urllib.quote(queryStr)
print encodedStr