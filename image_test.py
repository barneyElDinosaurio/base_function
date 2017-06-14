#coding=utf-8
#图像的基本测试
__author__ = 'vmplay'

from PIL import Image,ImageFilter
im=Image.open("C:\\git\\base_function\\original.jpg")
im2=Image.open("1.jpg")
(w,h)=im.size
print w,h
im.thumbnail((w/2,h/2))
im.save("small.jpg",'jpeg')
im2.filter(ImageFilter.BLUR)
im2.save("blur1.jpg",'jpeg')