# -*-coding=utf-8-*-
# @Time : 2018/8/21 13:47
# @File : captcha_usage.py

from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import numpy as np
import random
import string

characters = string.digits + string.ascii_uppercase
print(characters)
width,height,n_len,n_class=170,80,4,len(characters)
generator = ImageCaptcha(width=width,height=height)
rand_str = ''.join([random.choice(characters) for i in range(n_len)])
img = generator.generate_image(rand_str)
plt.imshow(img)
plt.title(rand_str)
plt.show()

def gen(batch_size=32):
    X = np.zeros((batch_size, height, width, 3), dtype=np.uint8)
    y = [np.zeros((batch_size, n_class), dtype=np.uint8) for i in range(n_len)]
    generator = ImageCaptcha(width=width, height=height)
    while True:
        for i in range(batch_size):
            random_str = ''.join([random.choice(characters) for j in range(4)])
            X[i] = generator.generate_image(random_str)
            for j, ch in enumerate(random_str):
                y[j][i, :] = 0
                y[j][i, characters.find(ch)] = 1
        yield X, y

