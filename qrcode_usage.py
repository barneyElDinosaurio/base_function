# -*-coding=utf-8-*-

# @Time : 2018/9/28 10:23
# @File : qrcode_usage.py
import cv2
import qrcode
import time
import matplotlib.pyplot as plt
from pyzbar import pyzbar


def create():
    qrcode.make('Make friend').get_image().show()
    time.sleep(20)

def recognize():
    file = 'barcode.jpg'
    image = cv2.imread(file)
    plt.imshow(image)
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x,y,w,h)=barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)




    # plt.show()
    # time.sleep(10)

# create()
recognize()