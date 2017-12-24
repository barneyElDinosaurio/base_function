import collections
from pandas import Series,DataFrame

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


def zip_case():
    x=['1','3','5','7','9']
    y=[2,4,6,8,10]
    z=zip(x,y)
    print z
    zd=dict(z)
    print zd
    #s=Series(zd)
    #print s
    #d=DataFrame(zd,index=[0])
    #d.to_csv('kk.csv',mode='a')

    uzip=zip(*z)
    print uzip
    uzip_x=uzip[0]
    uzip_y=uzip[1]

    x1=[('a','x'),('b','y')]

    print zip(*x1)

def set_case():
    a=['a','b','d','c','a']
    print a
    b=set(a)
    print b
    print 'type of b : ',type(b)


	
def dict_emulation():
	#print 'display'
	x=['a','b','c','d','d']
	y=[1,2,3,4,5]
	d=dict(zip(x,y))
	print d
	
	for k in d:
		print k
		print d[k]
		
	for k,v in d.items():
		print k,v
		
	for k,v in d.iteritems():
		print k,v


def baseDict():
    a={':authouer':'hello'}
    print a
def check_error():
    l=[{u'domain': u'.anjuke.com', u'secure': False, u'value': u'1', u'expiry': 1505201030, u'path': u'/', u'httpOnly': False, u'name': u'new_session'}, {u'domain': u'.anjuke.com', u'name': u'sessid', u'value': u'E886BE30-8244-2420-B6C0-78E4D38F6A71', u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.anjuke.com', u'secure': False, u'value': u'http%3A%2F%2Fshenzhen.anjuke.com%2Fcommunity%2Fp1%2F%7C', u'expiry': 1505231991.959638, u'path': u'/', u'httpOnly': False, u'name': u'lps'}, {u'domain': u'.anjuke.com', u'secure': False, u'value': u'13', u'expiry': 1507791229.959652, u'path': u'/', u'httpOnly': False, u'name': u'ctid'}, {u'domain': u'.anjuke.com', u'secure': False, u'value': u'1', u'expiry': 1505199530, u'path': u'/', u'httpOnly': False, u'name': u'__xsptplusUT_8'}, {u'domain': u'.anjuke.com', u'secure': False, u'value': u'D7D1D874-A066-7E07-A756-3766D45F5AF5', u'expiry': 1536821630.407441, u'path': u'/', u'httpOnly': False, u'name': u'aQQ_ajkguid'}, {u'domain': u'.anjuke.com', u'name': u'twe', u'value': u'2', u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.anjuke.com', u'secure': False, u'value': u'79092a60-0956-47e9-b60f-593683bb642c', u'expiry': 1536735230, u'path': u'/', u'httpOnly': False, u'name': u'58tj_uuid'}, {u'domain': u'.anjuke.com', u'secure': False, u'value': u'', u'expiry': 1505201030, u'path': u'/', u'httpOnly': False, u'name': u'init_refer'}, {u'domain': u'.anjuke.com', u'secure': False, u'value': u'1', u'expiry': 1536735230, u'path': u'/', u'httpOnly': False, u'name': u'new_uv'}, {u'domain': u'.anjuke.com', u'secure': False, u'value': u'8.1.1505199230.1505199230.1%234%7C%7C%7C%7C%7C%23%230rofZGQUhk1RMDrJQhVrTPQ8gCEjX3_a%23', u'expiry': 1568271230, u'path': u'/', u'httpOnly': False, u'name': u'__xsptplus8'}]
    print type(l)
    print len(l)
    for i in l:
        for k,v in i.items():
            print k,v
        print '\n'


#dict_assign()


#sclice_func()


#list_change()
#map_func()

#list_change()

#testcase1()
#testcase3()
#zip_case()
#set_case()
#dict_emulation()
#baseDict()
# check_error()
