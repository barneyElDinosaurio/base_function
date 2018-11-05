# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:44:27 2018

@author: xuduo
"""

import numpy as np
import cv2
import tensorflow as tf
import time
import base64

def Binarization(img): #img：图s片地址 
    # 读入图片
    for y in range(img.shape[1]):
        for x in range(img.shape[0]):
            if img[x, y][2] < 250:#使RGB值中R小于90的像素点变成纯黑
                img[x, y] = (0, 0, 0)
    for y in range(img.shape[1]):
        for x in range(img.shape[0]):
            if img[x, y][1] < 255:#使RGB值中G小于90的像素点变成纯黑
                img[x, y] = (0, 0, 0)
    for y in range(img.shape[1]):
        for x in range(img.shape[0]):
            if img[x, y][1] > 0:#使RGB值中B大于0的像素点变成纯白
                img[x, y] = (255, 255, 255)
    return img
            
def findUnicomArea(img):
    #先二值化
    UnicomArea = np.zeros(img.shape,np.int8)
    count = 0
    findpoint = []
    #首先遍历图像找到所有的联通区
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y][x] == 0 and UnicomArea[y][x] == 0):
                #这里表示已经找到了一个没有标志过的黑点，是一个新的联通区
                count += 1
                UnicomArea[y][x] = count
                findpoint.append((y,x))
            while len(findpoint) > 0:
                xx,yy = findpoint.pop()
                if yy + 1 < 159 and xx + 1 < 69:
                    if xx > 0 :#上面
                        if img[xx-1][yy] == 0 and UnicomArea[xx-1][yy] == 0:
                            findpoint.append((xx-1,yy))
                            UnicomArea[xx-1][yy] = count
                    if xx < img.shape[0]:#下面
                        if img[xx + 1][yy] == 0 and UnicomArea[xx + 1][yy] == 0:
                            findpoint.append((xx + 1, yy))
                            UnicomArea[xx+1][yy] = count
                    if yy > 0:#左面
                        if img[xx][yy-1] == 0 and UnicomArea[xx][yy-1] == 0:
                            findpoint.append((xx, yy-1))
                            UnicomArea[xx][yy-1] = count
                    if yy < img.shape[1]:#右面
                        if img[xx][yy+1] == 0 and UnicomArea[xx][yy+1] == 0:
                            findpoint.append((xx, yy+1))
                            UnicomArea[xx][yy+1] = count
    return count,UnicomArea

def separateUnicomArea (count,UnicomArea):
    #联通区任然存在一张表中，需要将其分离
    coutours = []
    desCoutous = []
    
    for num in range(1,count+1):
        coutours.append([])
        for x in range(UnicomArea.shape[0]):
            for y in range(UnicomArea.shape[1]):
                if UnicomArea[x][y] == num:
                    coutours[num-1].append([x,y,UnicomArea[x][y]])

    for num in range(len(coutours)):
        #将分离后的图像提取出来。计算出联通区所在的范围
        tmp = np.mat(coutours[num])
        minX = np.min(tmp[:,0])
        maxX = np.max(tmp[:,0])
        minY = np.min(tmp[:,1])
        maxY = np.max(tmp[:,1])
        pic_height = maxX - minX
        pic_width = maxY - minY
        img_temp = np.ones((pic_height+1, pic_width+1))
        temp_mat = np.empty((tmp.shape[0],3))
        temp_mat[:,0] = minX
        temp_mat[:,1] = minY
        temp_mat[:,2] = count
        small_X = tmp - temp_mat
        for a in range (small_X.shape[0]):
            first = int(small_X[a,0])
            second = int(small_X[a,1])
            img_temp[first][second] = 0
        desCoutous.append(img_temp)
    return desCoutous

def single_letter (single_pic):
    temp = []
    result = []
    for i in range(len(single_pic)):
        lenth = len(single_pic[i]) 
        if (lenth > 15):
            temp.append(single_pic[i])
    if len(temp) < 4 :
        pass
    else:
        for j in range(len(temp)):
            result.append(cv2.resize(temp[j],(48,48),interpolation=cv2.INTER_CUBIC))
            # print("cost",time.time()-cost)
        for k in range(len(result)):
            #cv2.imshow("test"+str(k),result[k])     #全黑图
            result[k] = result[k] * 255     #二值图
    return result

def make_data(letter):
    data = []
    data1 = np.asarray(letter[0])
    data2 = np.asarray(letter[1])
    data3 = np.asarray(letter[2])
    data4 = np.asarray(letter[3])
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)
    data = np.expand_dims(data,axis=3)
    return data


time_start=time.time()     

letter_dict = {0:'3',1:'4',2:'5',3:'6',4:'7',5:'8',6:'9',7:'a',8:'A',9:'b',10:'B',
               11:'C',12:'d',13:'e',14:'E',15:'f',16:'F',17:'g',18:'G',19:'h',20:'H',
               21:'i',22:'J',23:'K',24:'L',25:'m',26:'M',27:'n',28:'N',29:'P',30:'q',
               31:'Q',32:'r',33:'R',34:'S',35:'t',36:'T',37:'U',38:'V',39:'W',40:'X',
               41:'Y',42:'Z'}
predict = []
#import tensorflow as tf
#def load_model ():
#    with tf.Session() as sess:
#        saver = tf.train.import_meta_graph('F:/xd_finally/Captcha_pic/train/model/model6.0.ckpt.meta')
#        saver.restore(sess,tf.train.latest_checkpoint('F:/xd_finally/Captcha_pic/train/model/'))
#    return sess
def load_model ():
    sess = tf.Session()
    saver = tf.train.import_meta_graph('./model/model6.0.ckpt.meta')
    saver.restore(sess,tf.train.latest_checkpoint('./model'))
    return sess
    
#load_model()
def b64_to_np(b64_data):
    b64_decode=base64.b64decode(b64_data)    
    nparr=np.frombuffer(b64_decode,dtype=np.uint8)
    res=cv2.imdecode(nparr,cv2.COLOR_BGR2RGB)   
    img=np.asarray(res,dtype=np.uint8)
    return img

"""
修改1
"""
sess = load_model()
graph = tf.get_default_graph()
x = graph.get_tensor_by_name("x:0")
logits = graph.get_tensor_by_name("logits_eval:0")

def main (img_b64):
    img = b64_to_np(img_b64)
    Bin_img = Binarization(img)
    Bin_img = cv2.cvtColor(Bin_img,cv2.COLOR_BGR2GRAY)
    count,pic_UnicomArea = findUnicomArea(Bin_img)
    if count >= 4:
        single_pic= separateUnicomArea(count,pic_UnicomArea)
        letter = single_letter (single_pic)
        if len(letter)!=0:
            data = make_data(letter)

            feed_dict = {x:data}
            
            classification_result = sess.run(logits,feed_dict)
            output = []
            final_result = []

#            output = sess.run(tf.argmax(classification_result,1)) #修改2
            output = np.argmax(classification_result,1)
            for i in range(len(output)):
                final_result.append(letter_dict[output[i]])
            final_result =''.join(final_result)
            print("验证码预测为："+final_result)
        else:
            print('This pic can`t be recognized!')
            final_result = '101'
    elif count < 4:
        print('This pic have line!')
        final_result = '100'
    return final_result
    
#if __name__ == '__main__' :
    #img_path = 'F:/xd_finally/Captcha_pic/train/test/test2.png'
    #main(img_b64)
