# -*-coding=utf-8-*-

# @Time : 2018/10/10 9:56
# @File : xl_code.py

import requests
import urllib.request
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pytesseract
from sklearn.externals import joblib
import cv2
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


# 下载图片
def get_code(num=5000):
    url = 'https://web.credlink.com/xlzxins/auth/genCaptcha.do'
    for i in range(num):
        urllib.request.urlretrieve(url, 'test_{}.jpg'.format(i))


# 切割图片
def crop_image(img_name):
    img = Image.open(img_name)
    np_img = np.array(img)
    gray_img = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
    thresh, black_img = cv2.threshold(gray_img, 127, 255, 0)

    black_img_copy = black_img.copy()
    black_img_copy[0, :] = 255
    black_img_copy[-1, :] = 255
    black_img_copy[:, 0] = 255
    black_img_copy[:, -1] = 255

    (new_img, contours, hiera) = cv2.findContours(black_img_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnts = []
    for idx, c in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        print(x, y, w, h)
        if w > 5 and w < 15:
            cnts.append(black_img_copy[y:y + h, x:x + w])

    if len(cnts) != 4:
        return

    # 保存图片
    basename = img_name.split('.')[0]
    for idx, img_idx in enumerate(cnts):
        re_size_img = cv2.resize(img_idx, (15, 12), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("digits\\{}-{}.jpg".format(basename, idx), re_size_img)


def loop_dir():
    for file in os.listdir('.'):
        if os.path.isfile(file):
            crop_image(file)


def validation(filename):
    model = joblib.load('xlcaptcha.pkl')

    test_data = []

    # filename='test_0.jpg'
    # file=input_folder.format(0)+'\\test_4319-0.jpg'

    img = Image.open(filename).convert('RGB')
    np_img = np.array(img)
    gray_img = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
    thresh, black_img = cv2.threshold(gray_img, 127, 255, 0)
    # cv2.imshow('black',black_img)
    # cv2.waitKey(0)

    black_img_copy = black_img.copy()
    black_img_copy[0, :] = 255
    black_img_copy[-1, :] = 255
    black_img_copy[:, 0] = 255
    black_img_copy[:, -1] = 255
    (new_img, contours, hiera) = cv2.findContours(black_img_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted([(contour, cv2.boundingRect(contour)[0]) for contour in contours], key=lambda x: x[1])
    rets = []
    for c, b in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if w > 5 and w < 15:
            # cv2.imshow('kkk',black_img_copy[y:y+h,x:x+w])
            # cv2.waitKey(0)
            rets.append(black_img_copy[y:y + h, x:x + w])

    if len(rets) != 4:
        print('无法识别')
        return

    dataset = []
    for idx, i in enumerate(rets):
        t = cv2.resize(i, (15, 12), interpolation=cv2.INTER_AREA)
        # dataset.append(t.flatten())
        cv2.imwrite('{}.jpg'.format(idx), t)

    for i in range(4):
        img = Image.open('{}.jpg'.format(i)).convert('1')
        dataset.append([pixel for pixel in iter(img.getdata())])

    # print('dataset')
    # print('type of dateset {}'.format(type(dataset)))
    # print(dataset)
    # print('len of dataset {}'.format(len(dataset)))
    np_dataset = np.array(dataset)
    scaler = StandardScaler()
    scaler.fit(np_dataset)
    X_test_scaled = scaler.transform(np_dataset)
    y_predict = model.predict(X_test_scaled)
    for i in y_predict:
        print(i, end='')


#    X_test_scaled=scaler.transform(np_test_data)
#    result= model.predict(X_test_scaled)

# get_code()
# os.chdir('xl')
# loop_dir()
# filename='test_144.jpg'
def get_photo():
    url = 'https://web.credlink.com/xlzxins/auth/genCaptcha.do'
    filename = 'test.jpg'
    urllib.request.urlretrieve(url, filename)
    img = Image.open(filename)
    plt.imshow(img)
    plt.show()
    validation(filename)


# validation(filename)
get_photo()
print()
