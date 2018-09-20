# -*-coding=utf-8-*-

# @Time : 2018/9/20 11:25
# @File : rsa_demo.py

import rsa
import logging
import sys
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

format = logging.Formatter("%(asctime)s [%(levelname)s]:: %(message)s")    # output format 
sh = logging.StreamHandler(stream=sys.stdout)    # output to standard output
sh.setFormatter(format)
logger.addHandler(sh)
# 模反
def mofang():
    base=11
    n=13
    remain=0
    count=1
    while 1:
        if ((base*count-1)%n)==remain:
            print(count)
            # break
            count+=1
        else:
            count+=1

def get_key():
    a=9
    b=5
    remain=3937
    encryt_a=a**2987%remain
    encryt_b=b**2987%remain
    print('encryt a {}'.format(encryt_a))
    print('encryt b {}'.format(encryt_b))

    # 解密
    decryt_a = encryt_a**143%remain
    decryt_b = encryt_b**143%remain
    print('decryt a {}'.format(decryt_a))
    print('decryt b {}'.format(decryt_b))



def rsa_demo():
    (pubkey,privkey)=rsa.newkeys(1024)
    print('pubkey >>>> {}'.format(pubkey))
    print('privkey >>>> {}'.format(privkey))
    with open('pub.pem','w') as f:
        f.write(pubkey.save_pkcs1().decode())

    with open('priva.pem','w') as f:
        f.write(privkey.save_pkcs1().decode())

    message = 'Kill bill tonight'
    print("message encode {}".format(message.encode()))
    crypto=rsa.encrypt(message.encode(),pubkey)

    print('密文{}'.format(crypto))

    # 解密
    e_message = rsa.decrypt(crypto,privkey)
    print("解密后{}".format(e_message.decode()))


    private_sign = rsa.sign(message.encode(),privkey,'SHA-1')
    print('签名：{}'.format(private_sign))

    print('验证签名')
    print(rsa.verify(message.encode(),private_sign,pubkey))

# 生成器
def is_prime_number_generator(n):

    for i in range(2,n):
        if n%i==0:
            yield i
            # print(i)
            # return False
    else:
        yield None

def is_prime_number(n):

    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True


def cal_d():
    k=20
    e=25
    count=1
    while 1:
        if (count*e%k)==1:
            logger.info(count)
            break
        else:
            count+=1
        # logger.info(msg)

def custom_define_encry_decry():
    a=8
    b=7

    n=33
    d=24
    e=25

    encry_msg = a**e%n
    logger.info('原始数据为 {}'.format(a))
    logger.info('加密后的数据{}'.format(encry_msg))

    logger.info('开始解密>>>>>>>')

    decry_msg = encry_msg**d%n
    logger.info('解密后的数据为 {}'.format(decry_msg))

# mofang()
# rsa_demo()
# get_key()
# print(is_prime_number(3937))
# f=is_prime_number(3937)
# for i in f:
#     # print(next(f))
#     print(i)
# print(is_prime_number(199))
custom_define_encry_decry()
# cal_d()