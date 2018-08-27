# -*-coding=utf-8-*-
# @Time : 2018/8/21 9:00
# @File : captcha_code.py

from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import numpy as np
import random
import string
from keras.models import *
from keras.layers import *

# characters = string.digits + string.ascii_uppercase
characters = string.digits
print(characters)
width,height,n_len,n_class=170,80,4,len(characters)
generator = ImageCaptcha(width=width,height=height)
rand_str = ''.join([random.choice(characters) for i in range(n_len)])
img = generator.generate_image(rand_str)
# plt.imshow(img)
# plt.title(rand_str)
# plt.show()

def gen(batch_size=32):
    X = np.zeros((batch_size, height, width, 3), dtype=np.uint8)
    y = [np.zeros((batch_size, n_class), dtype=np.uint8) for i in range(n_len)]
    print('len of y {}'.format(len(y)))
    # print('shape of '.format())
    generator = ImageCaptcha(width=width, height=height)
    while True:
        for i in range(batch_size):
            random_str = ''.join([random.choice(characters) for j in range(4)])
            X[i] = generator.generate_image(random_str)
            for j, ch in enumerate(random_str):
                y[j][i, :] = 0
                y[j][i, characters.find(ch)] = 1
        yield X, y


def decode(y):
    y = np.argmax(np.array(y), axis=2)[:, 0]
    return ''.join([characters[x] for x in y])

def run_model():
    X, y = next(gen(1))
    # plt.imshow(X[0])
    # plt.title(decode(y))

    input_tensor = Input((height, width, 3))
    x = input_tensor
    for i in range(4):
        x = Convolution2D(32*2**i, 3, 3, activation='relu')(x)
        x = Convolution2D(32*2**i, 3, 3, activation='relu')(x)
        x = MaxPooling2D((2, 2))(x)

    x = Flatten()(x)
    x = Dropout(0.25)(x)
    x = [Dense(n_class, activation='softmax', name='c%d'%(i+1))(x) for i in range(4)]
    model = Model(input=input_tensor, output=x)

    model.compile(loss='categorical_crossentropy',
                  optimizer='adadelta',
                  metrics=['accuracy'])

    model.fit_generator(
                        gen(), samples_per_epoch=512, nb_epoch=8,
                        pickle_safe=False, nb_worker=4,
                        validation_data=gen(), nb_val_samples=1280
                        )

    X, y = next(gen(1))
    # model.save('20180822.pkl')
    y_pred = model.predict(X)
    model.save('20180823.pkl')
    plt.title('real: %s\npred:%s'%(decode(y), decode(y_pred)))

    # plt.imshow(X[0], cmap='gray')
    # plt.show()
    print(y_pred)


def load_model_pred():
    model = load_model('20180823.pkl')
    count=0
    while 1:
        X, y = next(gen(1))
        # model.save('20180822.pkl')
        y_pred = model.predict(X)
        # model.save('20180823.pkl')
        real_y,predit_y=decode(y), decode(y_pred)
        count+=1
        # print(y_pred)
        if real_y==predit_y:
            print('same')
            plt.title('real: %s\npred:%s' % (decode(y), decode(y_pred)))
            print('here: successful ration: {}'.format(100/count))
            plt.imshow(X[0], cmap='gray')
            plt.show()

            break

# run_model()
load_model_pred()