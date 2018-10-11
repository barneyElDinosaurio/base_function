#-*-coding=utf-8-*-
# from PIL import Image
from claptcha import Claptcha

def testcase():
    im=Image.open('captcha.gif')
    data=im.convert('P')
    hist= im.histogram()
    print(data)
    values={}
    for i in range(256):
        values[i]=hist[i]

    print(values)
    for k,v in sorted(values.items(),reverse=True):
        print(k,v)


def case3():
    c = Claptcha("8069",'C:\\Windows\winsxs\\amd64_microsoft-windows-f..etype-timesnewroman_31bf3856ad364e35_6.1.7601.17514_none_3b958c66aff6cdb7\\times.ttf')
    t,_ = c.write('code1.png')

case3()
# testcase()

