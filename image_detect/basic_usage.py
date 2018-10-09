# -*-coding:utf-8-*-
# 图像的基本测试

import time
import os
# from urllib import request
import requests
from PIL import ImageFilter, ImageDraw,ImageEnhance,Image,ImageFilter
import re
import random
import pytesseract
import numpy as np
import cv2
import matplotlib.pyplot as plt

def base_usage():
    im = Image.open("data/original.jpg")
    im2 = Image.open("data/original.jpg")
    print(im)
    im = im.convert('L')
    print(im)
    image_data = im.getdata()
    print(image_data)
    # im.show()
    (w, h) = im.size
    print(w, h)
    im.thumbnail((w / 2, h / 2))
    im.save("data/small.jpg", 'jpeg')
    im2.filter(ImageFilter.BLUR)
    im2.save("data/blur3.jpg", 'jpeg')


def read_image():
    im = Image.open('data/len_full.jpg')
    print(im.mode)
    # print(im.getpixel((0,0)))
    bw = im.convert('1')
    x, y = bw.size
    print(x, y)
    grey = im.convert('L')
    for i in range(x):
        for j in range(y):
            pass
            # print(bw.getpixel((i,j)))
    bw.show()
    grey.show()
    data = grey.getdata()
    new_data = np.matrix(data)
    print(new_data)

    dt = np.reshape(new_data, (855, 400))
    print(dt)
    for i in range(855 - 1):
        for j in range(400 - 1):
            if random.random() > 0.5:
                dt[i, j] = 0
    new_im = Image.fromarray(dt)
    new_im.show()


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
            # f = open(u"Verification.txt", "w")
            # f.write(str(text))
            # f.close()

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
    for i in range(3000):
        url = 'http://113.108.219.40/Dop/CheckCode.aspx?codemark=38.63767845258748'
        # request.urlretrieve(url,'code.png')
        r = requests.get(url)
        with open(str(i) + '.gif', 'wb') as f:
            f.write(r.content)


def change_color():
    # get_image()
    img = Image.open('Check.gif')
    # img.show()
    width = img.size[0]  # 长度
    height = img.size[1]  # 宽度
    img = img.crop((2, 4, width - 2, 19))
    img.show()
    img = img.convert('RGB')
    width = img.size[0]  # 长度
    height = img.size[1]  # 宽度

    print(width, height)
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
    enchancer = ImageEnhance.Contrast(img)
    img = enchancer.enhance(1)
    img = img.convert('L')
    target = 'D2T4J'
    img.show()
    text = pytesseract.image_to_string(img)
    print(text)
    if target == text:
        print('Bingo')


def split_photo():
    os.chdir('data')
    x1 = 5
    y1 = 3
    x2 = 65
    y2 = 21
    for num in range(3000):
        im = Image.open(str(num) + '.gif')
        im = im.crop((x1, y1, x2, y2))
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
        im = im.convert('L')
        im.save(str(num) + '-crop.gif')


def split_photo_piece():
    os.chdir('data')
    for num in range(3000):
        im = Image.open(str(num) + '-crop.gif')
        width = im.size[0]  # 长度
        each_width = width / 5
        height = im.size[1]  # 宽度
        for i in range(5):
            im_x = im.crop((each_width * i, 0, each_width * (i + 1), height))
            # im_x=im_x.convert('RGB')
            # im_x=im_x.convert('L')
            im_x.save(str(num) + '-crop-{}'.format(i) + '.gif')

# 使用opencv 切割
def split_photo_cv():
    img = Image.open('shibiecuowu1537546979.png')
    # plt.imshow(img)
    # plt.title('color')
    # plt.show()

    img = img.convert('RGB')

    width = img.size[0]  # 长度
    height = img.size[1]  # 宽度

    #仅对某种验证码有效
    # print(width, height)
    # for i in range(0, width):  # 遍历所有长度的点
    #     for j in range(0, height):  # 遍历所有宽度的点
    #         data = (img.getpixel((i, j)))  # 打印该图片的所有点
    #         # print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
    #         # print(data[0])  # 打印RGBA的r值
    #         # print(data[1])
    #         if data[1] > 200:
    #             # data[1]=0
    #             # r=data[0]
    #             img.putpixel((i, j), (255, 255, 255))  # 则这些像素点的颜色改成大红色

    # plt.imshow(img)
    # plt.title('remove noise')
    # plt.show()

    g_img = img.convert('L')
    # plt.imshow(g_img)
    # plt.title('gray')
    # plt.show()

    np_img = np.array(g_img)
    ret,thres_img = cv2.threshold(np_img,0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # ret,thres_img = cv2.threshold(np_img,0, 255,cv2.THRESH_BINARY+cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print(ret)
    # thres_img = cv2.adaptiveThresh(np_img,127, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,5)
    # plt.imshow(thres_img)
    # plt.title('black')
    # plt.show()

    print(pytesseract.image_to_string(thres_img))

    # 切割

    img,contour,hier = cv2.findContours(thres_img.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contour], key=lambda x: x[1])
    rets = []
    for c, b in cnts:
        x, y, w, h = cv2.boundingRect(c)
        print(x, y, w, h)
        rets.append((x, y, w, h))
        # if h >= 14:
        #     if w > 14*2 and w < 14*3:
        #         rets.append((x, y, int(w/2), h))
        #         rets.append((x+int(w/2), y, int(w/2), h))
        #     elif w < 14*3:
        #         rets.append((x, y, w, h))

        #     if w > 20:
        #         rets.append((x, y, int(w / 2), h))
        #         rets.append((x, y + int(w / 2), int(w / 2), h))
        #     else:
        #         rets.append((x, y, w, h))

    for idx, cord in enumerate(rets):
        print(cord)
        (x, y, w, h) = cord
        # plt.imsave('10091-{}.jpg'.format(idx), thres_img[y:y + h, x:x + w])
        # print(pytesseract.image_to_string(thres_img[y:y + h, x:x + w]))
        cv2.imshow('{}'.format(idx),thres_img[y:y + h, x:x + w])
        cv2.waitKey(0)

def single_word():
    import string, shutil, re
    os.chdir('data')

    for i in os.listdir('.'):
        if os.path.isfile(i) and re.search('(\d+)-crop-(\d+).gif', i):
            # print(i)

            im = Image.open(i)
            im = im.convert('L')
            text = pytesseract.image_to_string(im, config='-psm 10')
            print(text)
            if text in string.ascii_uppercase or text in string.digits or text in string.ascii_lowercase:
                print('find one')
                print(text.upper() + '/' + i)
                try:
                    shutil.copy(i, os.path.join(text.upper(), i))
                except:
                    continue


def flood_noise():
    def check(j, i):
        try:
            if pix[j, i] == 0 and matrix[j][i] != -1:
                return True
            else:
                return False
        except:
            return False


def juli(r, s):
    return abs(r[0] - s[0]) + abs(r[1] - s[1]) + abs(r[2] - s[2])


def sample():
    im = Image.open('code.gif')
    width = im.size[0]  # 长度
    height = im.size[1]  # 宽度
    im = im.convert('RGB')
    for i in range(0, width):  # 遍历所有长度的点
        for j in range(0, height):  # 遍历所有宽度的点
            data = (im.getpixel((i, j)))  # 打印该图片的所有点
            # print(data)
            if data[1] > 155:
                # data[1]=0
                # r=data[0]
                im.putpixel((i, j), (255, 255, 255))  # 则这些像素点的颜色改成白色

            # if data[2] < 0:
            #     im.putpixel((i,j),(255,255,255))
    # im = ImageEnhance.Sharpness(im).enhance(9)
    # im.show()
    im = im.convert('L')
    im.save('no-greed-code.gif')
    return im


def getPixel(image, x, y, G, N):
    L = image.getpixel((x, y))
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0
    if L == (image.getpixel((x - 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x, y - 1))
    else:
        return None

    # 降噪


# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# G: Integer 图像二值化阀值
# N: Integer 降噪率 0 <N <8
# Z: Integer 降噪次数
# 输出
#  0：降噪成功
#  1：降噪失败
def clearNoise(image, G, N, Z):
    draw = ImageDraw.Draw(image)

    for i in range(0, Z):
        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                color = getPixel(image, x, y, G, N)
                if color != None:
                    draw.point((x, y), color)


def run_remove_noise():
    im = sample()
    w = im.size[0]
    h = im.size[1]

    for i in range(w):
        for j in range(h):
            r = [0, 0, 0]
            s = [0, 0, 0]
            if pix[j, i] == 0:
                if check(j - 1, i):
                    r[0], r[1], r[2] = im2.getpixel((j, i))
                    s[0], s[1], s[2] = im2.getpixel((j - 1, i))
                    print
                    r
                    print
                    s
                    print
                    "-" * 55
                    if juli(r, s) <= l:
                        matrix[j][i] = matrix[j - 1][i]
                        maps[str(matrix[j][i])] += 1
                elif check(j - 1, i - 1):
                    r[0], r[1], r[2] = im2.getpixel((j, i))
                    s[0], s[1], s[2] = im2.getpixel((j - 1, i - 1))
                    if juli(r, s) <= l:
                        matrix[j][i] = matrix[j - 1][i - 1]
                        maps[str(matrix[j][i])] += 1
                elif check(j, i - 1):
                    r[0], r[1], r[2] = im2.getpixel((j, i))
                    s[0], s[1], s[2] = im2.getpixel((j - 1, i))
                    if juli(r, s) <= l:
                        matrix[j][i] = matrix[j][i - 1]
                        maps[str(matrix[j][i])] += 1
                elif check(j + 1, i + 1):
                    r[0], r[1], r[2] = im2.getpixel((j, i))
                    s[0], s[1], s[2] = im2.getpixel((j + 1, i + 1))
                    if juli(r, s) <= l:
                        matrix[j][i] = matrix[j + 1][i + 1]
                        maps[str(matrix[j][i])] += 1
                elif check(j, i + 1):
                    r[0], r[1], r[2] = im2.getpixel((j, i))
                    s[0], s[1], s[2] = im2.getpixel((j, i + 1))
                    if juli(r, s) <= l:
                        matrix[j][i] = matrix[j][i + 1]
                        maps[str(matrix[j][i])] += 1
                elif check(j - 1, i + 1):
                    pr[0], r[1], r[2] = im2.getpixel((j, i))
                    s[0], s[1], s[2] = im2.getpixel((j - 1, i + 1))
                    if juli(r, s) <= l:
                        matrix[j][i] = matrix[j - 1][i + 1]
                        maps[str(matrix[j][i])] += 1
                elif check(j + 1, i - 1):
                    r[0], r[1], r[2] = im2.getpixel((j, i))
                    s[0], s[1], s[2] = im2.getpixel((j + 1, i - 1))
                    if juli(r, s) <= l:
                        matrix[j][i] = matrix[j + 1][i - 1]
                        maps[str(matrix[j][i])] += 1
                elif check(j + 1, i):
                    r[0], r[1], r[2] = im2.getpixel((j, i))
                    s[0], s[1], s[2] = im2.getpixel((j + 1, i))
                    if juli(r, s) <= l:
                        matrix[j][i] = matrix[j + 1][i]
                        maps[str(matrix[j][i])] += 1
                else:
                    n += 1
                    maps[str(n)] = 1
                    matrix[j][i] = n

    for i in range(w):
        for j in range(h):
            if matrix[j][i] != -1 and maps[str(matrix[j][i])] <= 2:
                im.putpixel((j, i), 255)


def calc_ration(filename):
    im = Image.open(filename)
    im = im.convert('RGB')
    (w, h) = im.size
    R, G, B = 0, 0, 0
    for i in range(w):
        for j in range(h):
            (r, g, b) = im.getpixel((i, j))
            R += r
            G += g
            B += b
    return R / (R + G + B), G / (R + G + B), B / (R + G + B)


def calc_all():
    for i in os.listdir('.'):
        if os.path.isfile(i) and re.search('\d{4}.gif', i):
            print(calc_ration(i))


def remove_noise():
    filename = '2999.gif'
    R, G, B = calc_ration(filename)
    print(R, G, B)
    im = Image.open(filename)
    im = im.convert('RGB')
    (w, h) = im.size
    for i in range(w):
        for j in range(h):
            (r, g, b) = im.getpixel((i, j))
            n = (r * R + g * G + b * B)
            print(n)
            if n > 120:
                im.putpixel((i, j), (255, 255, 255))
            else:
                im.putpixel((i, j), (0, 0, 0))
    im.convert('1')
    text = pytesseract.image_to_string(im)
    print(text)
    im.show()


def folder_detect():
    for i in os.listdir('.'):
        if i.endswith('.gif'):
            im = Image.open(i)

            im = im.convert('L')
            text = pytesseract.image_to_string(im)
            try:
                print(text)
                if text.upper() == 'J4V2V':
                    print('found file {}'.format(i))
            except:
                continue


def find_best_args():
    # 去噪,G = 50,N = 4,Z = 4
    for i in range(1, 250, 5):
        for j in range(1, 9):
            for k in range(1, 9):
                image = Image.open("test-no-green.gif")

                # 将图片转换成灰度图片
                image = image.convert("L")
                clearNoise(image, i, j, k)

                image.save('test-no-green-{}-{}-{}.gif'.format(i, j, k))


def validation():
    image = Image.open('15-crop.gif')
    image = image.convert('L')
    clearNoise(image, 131, 2, 2)
    text = pytesseract.image_to_string(image)
    print(text)


def clear_noise2():
    img = Image.open('g.jpg')
    clearNoise(img, 50, 1, 4)
    img.show()

# 轮廓的使用 csdn 例子
def contour_usage():

    img = cv2.imread('contour.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    cv2.imshow('black',thresh)
    cv2.waitKey(0)
    img_,contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('after contour',img_)
    cv2.waitKey(0)

    print('len of contours ',len(contours))
    print('index 0 contours ',len(contours[0]))
    print('index 1 contours ',len(contours[1]))
    # print('index 2 contours ',len(contours[2]))
    # print('index 3 contours ',len(contours[3]))
    print(contours, '--------')
    print(hierarchy, '********')
    output = np.zeros(img.shape, dtype=np.uint8)
    cv2.drawContours(output, contours, -1, (0, 255, 0), 2)
    cv2.imshow('whole', output)
    cv2.waitKey(0)
    output[:] = 0

    flag = [1, ] * len(contours)
    for i in range(len(contours)):
        contour = contours[i].copy()
        index = i
        while flag[index] == 1:
            cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)  # contours is a list
            flag[index] = 0
            print(index)
            index = hierarchy[0][index][0]  # dimension array
            cv2.imshow('stepbystep', output)
            cv2.waitKey(0)
            if index == -1:
                print(index)
                break
            else:
                contour = contours[index]

# 修改
def contour_usage2():

    img = cv2.imread('contour.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    cv2.imshow('black',thresh)
    cv2.waitKey(0)
    img_,contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('after contour',img_)
    cv2.waitKey(0)
    offet=50
    for i in range(len(contours)):
        (x,y,w,h)=cv2.boundingRect(contours[i])

        cv2.imshow('{} pic'.format(i),img[y-offet:y+w+offet,x-offet:x+h+offet])
        cv2.waitKey(0)

    time.sleep(5)

# 官方教程 画轮廓
def contour_usage3():

    img = cv2.imread('tw_photo.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    # cv2.imshow('black',thresh)
    # cv2.waitKey(0)
    img_,contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow('after contour',img_)
    # cv2.waitKey(0)
    print('len of ',len(contours))
    for i in range(len(contours)):
        cnt = contours[i]
        output = np.zeros(img.shape, dtype=np.uint8)
        output[:] = 0

        cv2.drawContours(output,[cnt],0,(0,255,0),3)
        cv2.imshow('draw',output)
        cv2.waitKey(0)

def main():
    # os.chdir('data/temp')
    # base_usage()
    # read_image()
    # image_recognize()
    # get_image()
    # change_color()
    # conver_gif()
    # split_photo()
    # split_photo_piece()
    # single_word()
    # im = sample()
    # print(calc_ration())
    # remove_noise()
    # calc_all()
    # folder_detect()
    # validation()
    # find_best_args()
    # sample()
    # clear_noise2()
    split_photo_cv()
    # contour_usage2()
    # contour_usage3()

if __name__ == '__main__':
    main()
