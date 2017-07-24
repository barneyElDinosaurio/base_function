#-*-coding=utf-8-*-
from PIL import Image

def testcase():
    im=Image.open('captcha.gif')
    data=im.convert('P')
    hist= im.histogram()
    print data
    values={}
    for i in range(256):
        values[i]=hist[i]

    print values
    for k,v in sorted(values.items(),reverse=True):
        print k,v
testcase()

