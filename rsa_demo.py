# -*-coding=utf-8-*-

# @Time : 2018/9/20 11:25
# @File : rsa_demo.py

import rsa
import logging
import sys
import base64

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
    x=1
    while 1:
        if (17*x-1)%3120==0:
            print(x)
            # break
            x+=1
        else:
            x+=1


def custom_define_encry_decry():
    # a=30
    # b=7
    #
    # n=33
    # d=97
    # e=13

    a=3333
    n=3233
    e=17
    d=2753
    encry_msg = (a**e)%n
    logger.info('原始数据为 {}'.format(a))
    logger.info('加密后的数据{}'.format(encry_msg))

    logger.info('开始解密>>>>>>>')

    decry_msg = (encry_msg**d)%n
    logger.info('解密后的数据为 {}'.format(decry_msg))

# 计算d的值
def cal_mofang():
    # 13X+1=20Y
    pass

# 因数分解
def factor_split():
    t=1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413
    print(t)
    a=33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489
    print(t%a)


# py2
def web_demo():


    def str2key(s):
        # 对字符串解码
        b_str = base64.b64decode(s)
        # print(b_str)

        if len(b_str) < 162:
            return False

        hex_str = ''
        # b_str=s
        # 按位转换成16进制
        for x in b_str:
            # print(x)
            # print(type(x))
            h = hex(ord(x))[2:]
            h = h.rjust(2, '0')
            hex_str += h

        # 找到模数和指数的开头结束位置
        m_start = 29 * 2
        e_start = 159 * 2
        m_len = 128 * 2
        e_len = 3 * 2

        modulus = hex_str[m_start:m_start + m_len]
        exponent = hex_str[e_start:e_start + e_len]

        return modulus,exponent


    pubkey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDC7kw8r6tq43pwApYvkJ5laljaN9BZb21TAIfT/vexbobzH7Q8SUdP5uDPXEBKzOjx2L28y7Xs1d9v3tdPfKI2LR7PAzWBmDMn8riHrDDNpUpJnlAGUqJG9ooPn8j7YNpcxCa1iybOlc2kEhmJn5uwoanQq+CA6agNkqly2H4j6wIDAQAB"
    key = str2key(pubkey)
    print(key)

# py2
def web_demo2():
    import binascii
    def en_test():
        param_1 = "010001"
        # 某次我找到的
        param_2 = "955120AB9334B7CD52FCDB422DBF564AFD46DEBDC706F33502BBFAD9DD216A22E4D5012CB70F28473B46FB7190D08C31B4B8E76B5112ACE1C5552408961530B1C932DEEA8FC38A9A624AD22073F56F02BF453DD2C1FEA0164106D6B099CC9E5EC88C356FC164FCA47C766DD565D3D11048D27F2DD4221A0B26AB59BD7D09841F"
        message = 'nihao'
        modulus = int(param_2, 16)
        exponent = int(param_1, 16)
        rsa_pubkey = rsa.PublicKey(modulus, exponent)
        crypto = rsa.encrypt(message, rsa_pubkey)
        data = binascii.b2a_hex(crypto)

        print(data)

    en_test()

# mofang()
# rsa_demo()
# get_key()
# print(is_prime_number(3937))
# f=is_prime_number(3937)
# for i in f:
#     # print(next(f))
#     print(i)
# print(is_prime_number(199))
# custom_define_encry_decry()
# cal_d()
# factor_split()
# custom_define_encry_decry()
# web_demo()
web_demo2()