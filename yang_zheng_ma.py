#coding=utf-8
__author__ = 'vmplay'
# 生成验证码 四个字母
import random, Image, ImageFont, ImageDraw, ImageFilter


def rndcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def rndchar():
    return chr(random.randint(65, 90))


h = 60
w = h * 4
image = Image.new('RGB', (w, h), (255, 255, 0))
fonts = ImageFont.truetype("arial.ttf", 36)
draw = ImageDraw.Draw(image)
for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=rndcolor())
for t in range(4):
    # draw.text((60*t+10,10),rndchar(),font=fonts,fill=rndcolor2())
    draw.text((60 * t + 10, 10), rndchar(), font=fonts, fill=rndcolor2())
image = image.filter(ImageFilter.BLUR)
image.save("1.jpg", 'jpeg')
