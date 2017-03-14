#-*-coding=utf-8-*-
__author__ = 'xda'
import urllib2
try:
    #Normal execution block
    open('data.cfg','r')
except urllib2.UnknownHandler,e:
    #Exception A handle
    print "can't find"
except urllib2.URLError,e:
    #Exception B handle
    print "still error"
except urllib2.UnknownHandler,e:
    #Other exception handle
    print "error"
else:
    #if no exception,get here
    print "open"
finally:
    print "finally"