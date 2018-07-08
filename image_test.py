#coding=utf-8
__author__ = 'rocky'

#图像的基本测试
import random
import pytesseract
from PIL import Image
from PIL import Image,ImageFilter
import numpy as np

def base_usage():
    im=Image.open("data/original.jpg")
    im2=Image.open("data/original.jpg")
    print(im)
    im=im.convert('L')
    print(im)
    image_data = im.getdata()
    print(image_data)
    #im.show()
    (w,h)=im.size
    print(w,h)
    im.thumbnail((w/2,h/2))
    im.save("data/small.jpg",'jpeg')
    im2.filter(ImageFilter.BLUR)
    im2.save("data/blur3.jpg",'jpeg')

def read_image():
    im = Image.open('data/len_full.jpg')
    print(im.mode)
    # print(im.getpixel((0,0)))
    bw = im.convert('1')
    x,y = bw.size
    print(x,y)
    grey = im.convert('L')
    for i in range(x):
        for j in range(y):
            pass
            #print(bw.getpixel((i,j)))
    bw.show()
    grey.show()
    data = grey.getdata()
    new_data = np.matrix(data)
    print(new_data)

    dt = np.reshape(new_data,(855,400))
    print(dt)
    for i in range(855-1):
        for j in range(400-1):
            if random.random()>0.5:
                dt[i,j]=0
    new_im = Image.fromarray(dt)
    new_im.show()


def image_recognize():

    class GetImageDate(object):
        def m(self):
            image = Image.open("captchaNew.jpg")
            text = pytesseract.image_to_string(image)
            return text

        def SaveResultToDocument(self):
            text = self.m()
            print(text)
            f = open(u"Verification.txt", "w")
            f.write(str(text))
            f.close()

    g = GetImageDate()
    g.SaveResultToDocument()


def main():
    # base_usage()
    # read_image()
    image_recognize()

if __name__=='__main__':
    main()