#-*-coding=utf-8-*-
__author__ = 'rocky'
import hashlib
import hmac
import base64

def testcase1():
    message=bytes('Message').encode('utf-8')
    print type(message)
    print message

    secret=bytes('secret').encode('utf-8')
    sha=hmac.new(secret,message,digestmod=hashlib.sha256).digest()
    print type(sha)
    print sha
    signature=base64.b64encode(sha)
    print signature

def testcase2():
    t1=hashlib.sha1('Hello World').hexdigest()
    print t1
#testcase1()
testcase2()