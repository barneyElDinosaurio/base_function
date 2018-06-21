#-*-coding:utf-8-*-
import time
import os
from PIL import Image
import pytesseract
# from urllib import request
import requests
from PIL import ImageFilter
from PIL import ImageEnhance

def image_recognize():
    class GetImageDate(object):
        def m(self):
            image = Image.open("CheckCode.png")
            image.show()

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


def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def conver_gif():
    im = Image.open('Check.gif')
    im.show()
    im.convert('RGB')


def get_image():
    os.chdir('data')
    for i in range(1000):
        url = 'http://113.108.219.40/Dop/CheckCode.aspx?codemark=38.63767845258748'
    # request.urlretrieve(url,'code.png')
        r = requests.get(url)
        with open(str(i)+'.gif', 'wb') as f:
            f.write(r.content)


def change_color():
    # get_image()
    img = Image.open('Check.gif')
    # img.show()
    width = img.size[0]  # 长度
    height = img.size[1]  # 宽度
    img=img.crop((2,4,width-2,19))
    img.show()
    img = img.convert('RGB')
    width = img.size[0]  # 长度
    height = img.size[1]  # 宽度

    print(width,height)
    for i in range(0, width):  # 遍历所有长度的点
        for j in range(0, height):  # 遍历所有宽度的点
            data = (img.getpixel((i, j)))  # 打印该图片的所有点
            # print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            # print(data[0])  # 打印RGBA的r值
            # print(data[1])
            if data[1] > 200:
                # data[1]=0
                # r=data[0]
                img.putpixel((i, j), (255, 255, 255))  # 则这些像素点的颜色改成大红色

    #         if (data[0] >= 170 and data[1] >= 170 and data[2] >= 170):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
    #             img.putpixel((i, j), (234, 53, 57, 255))  # 则这些像素点的颜色改成大红色
    # img = img.convert("RGB")  # 把图片强制转成RGB
    # img=img.filter(ImageFilter.MedianFilter())
    enchancer =ImageEnhance.Contrast(img)
    img=enchancer.enhance(1)
    img=img.convert('L')
    target = 'D2T4J'
    img.show()
    text = pytesseract.image_to_string(img)
    print(text)
    if target == text:
        print('Bingo')

def split_photo():
    os.chdir('data')
    x1=5
    y1=4
    x2=65
    y2=20
    for num in range(1000):
        im=Image.open(str(num)+'.gif')
        im=im.crop((x1,y1,x2,y2))
        width = im.size[0]  # 长度
        height = im.size[1]  # 宽度
        im = im.convert('RGB')
        for i in range(0, width):  # 遍历所有长度的点
            for j in range(0, height):  # 遍历所有宽度的点
                data = (im.getpixel((i, j)))  # 打印该图片的所有点
                # print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
                # print(data[0])  # 打印RGBA的r值
                # print(data[1])
                if data[1] > 200:
                    # data[1]=0
                    # r=data[0]
                    im.putpixel((i, j), (255, 255, 255))  # 则这些像素点的颜色改成白色
        im.save(str(num)+'-crop.gif')

def split_photo_piece():
    os.chdir('data')
    for num in range(1000):
        im=Image.open(str(num)+'-crop.gif')
        width = im.size[0]  # 长度
        each_width = width/5
        height = im.size[1]  # 宽度
        for i in range(5):
            im_x=im.crop((each_width*i,0,each_width*(i+1),height))
            # im_x=im_x.convert('RGB')
            im_x=im_x.convert('L')
            im_x.save(str(num)+'-crop-{}'.format(i)+'.gif')

def single_word():
    import string,shutil
    os.chdir('data/split_data')

    for i in os.listdir('.'):
        if os.path.isfile(i):
            # print i
            im=Image.open(i)
            text=pytesseract.image_to_string(im,config='-psm 10')
            print text
            if text in string.ascii_uppercase or text in string.digits or text in string.ascii_lowercase:
                print 'find one'
                print text.upper()+'/'+i
                shutil.copy(i,os.path.join(text.upper(),i))

def main():
    # base_usage()
    # read_image()
    # image_recognize()
    # get_image()
    # change_color()
    # conver_gif()
    # split_photo()
    # split_photo_piece()
    single_word()

if __name__ == '__main__':
    main()
