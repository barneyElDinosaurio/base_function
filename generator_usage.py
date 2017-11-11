#-*-coding=utf-8-*-
# 迭代器的使用

# 生成器解析器
def genlist():
    x = (i**2 for i in range(10))
    print x.next()
    print x.next()
    print x.next()

def gensquart(N):
    for i in range(N):
        yield i**3

def testcase():
    x = gensquart(10)
    '''
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    '''
    while 1:
        try:
            print x.next()
        except StopIteration:
            print 'stop'
            break

    for i in gensquart(11):
        print i

    genlist()

class MyGenerator():
    def __init__(self,n):
        self.end=n
        self.current =-1
        self.content = []
        for i in range(self.end):
            self.content.append(i**3)
    def __iter__(self):
        return self

    def next(self):
         self.current=self.current+1
         return self.content[self.current]




def testcase2():
    obj = MyGenerator(10)
    '''
    print obj.next()
    print obj.next()
    print obj.next()
    print obj.next()
    '''
    for i in MyGenerator(10):
        print i


testcase2()