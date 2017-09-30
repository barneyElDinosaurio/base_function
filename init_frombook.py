#-*-coding=utf-8-*-
class X:
    pass
# python2 非法
#X.__class__

class Rectangle:
    def area(self):
        # 居然可以不用初始化， 类实例化后可以直接赋值
        # 不好的习惯， 避免
        return self.width*self.height

rec=Rectangle()
rec.width, rec.height=10, 20
print rec.area()