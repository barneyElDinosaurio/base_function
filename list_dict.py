import collections


def list_dict():
    s = [("yellow", 1), ("red", 2), ("white", 3), ("black", 4), ("green", 5)]
    d = collections.defaultdict(list)
    for k, v in s:
        print "k is %s, v is %d" % (k, v)
        # d[k]=v

        d[k].append(v)

    print d

    print d
    for k in d:
        print "k is %s, v is " % k
        print d[k][0]

    print "*" * 10
    s = 'mississippi'
    d = collections.defaultdict(int)
    for k in s:
        # print k
        d[k] += 1

    print d

    print 'I\'m {},{}'.format("hongten", "welcome to you")

    mydict = collections.defaultdict(list)
    s = [("a", [1, 2, 3, 4]), ("b", [2, 3, 4, 5]), ("c", [3, 4, 5, 6]), ("d", [4, 5, 6, 7])]
    for k, v in s:
        mydict[k] = v

    print mydict


def dict_assign():
    a = {}
    b = a
    a["a"] = "1"
    print b
    x = 1
    y = x
    x = 2
    print y
    a["a"] = "2"
    print b
    print id(a)
    print id(b)
    list = [1, 2, 3, 5, 4, 6, 434, 2323, 333, 99999]
    print "max of list is ",
    print max(list)


def sclice_func():
    a = [1, 3, 5, 7, 9, 11, 23, 1, 2]
    b = a[-1:-6:-1]
    print b

# dict_assign()
#sclice_func()


def list_change():
    a = [1, 2, 3, 4]
    print a
    for i in range(len(a)):
        a[i] = a[i] + 1

    print a


def test_func(x):
    return x * x


def map_func():
    a = [1, 2, 3, 4, 5]
    b = map(test_func, a)
    print b


def get_float(x):
    return x*1.00

def testcase1():
    x1=range(0,100)
    print "before map\n",x1

    x2=map(get_float,x1)
    print "After map\n",x2



def testcase2():
    x=range(0,200)
    y=filter(lambda t:t%2==0,x)
    print y

def reduce_case(x,y):
    return x+y

def testcase3():
    x=range(0,200)
    y=reduce(reduce_case,x)
    print y
#dict_assign()


#sclice_func()


#list_change()
#map_func()

#list_change()

#testcase1()
testcase3()
