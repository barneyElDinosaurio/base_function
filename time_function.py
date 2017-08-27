# -*-coding=utf-8-*-
# 日期函数的使用
import time, datetime


class Data_test(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    def out_date(self):
        print "year :"
        print self.year
        print "month :"
        print self.month
        print "day :"
        print self.day


class Data_test2(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, data_as_string):
        year, month, day = map(int, string_date.split('-'))
        date1 = cls(year, month, day)
        return date1

    def out_date(self):
        print "year :"
        print self.year
        print "month :"
        print self.month
        print "day :"
        print self.day
        print "Done"


class DateTest3():
    def getPreviousDay(self):
        now = datetime.datetime.now()
        print type(now)
        last = now + datetime.timedelta(days=-3)
        #日期增减
        print last
        print   last.strftime("%Y-%m-%d")


def time_string_test():
    print "Test"
    file_name = "hello.txt"
    f = open(file_name, 'a')
    now = datetime.datetime.now()
    print now
    print type(now)
    #f.write(now)

    now2 = time.strftime("%Y-%m-%d %H:%M:%S")
    print now2
    print type(now2)

    now3 = now.strftime("%Y-%m-%d %H:%M:%S")
    print now3
    print type(now3)
    now4=now.strftime("%Y%m%d%H%M%S")
    print now4
    f.close()


def test1():
    t = Data_test(2016, 8, 1)
    t.out_date()
    string_date = '2016-8-1'
    year, month, day = map(int, string_date.split('-'))
    s = Data_test(year, month, day)
    s.out_date()
    print "@Class"
    r = Data_test2.get_date("2016-8-6")
    r.out_date()

    print "*" * 10
    d3 = DateTest3()
    d3.getPreviousDay()


def test2():
    now = time.strftime("%Y-%m-%d")
    print now
    print type(now)
    now_time = datetime.datetime.now()
    print now_time
    print type(now_time)
    today = time.strftime("_%Y_%m_%d")

    print today

    aa = datetime.datetime(2016, 8, 7)
    #看输入的日期是一个星期的第几天
    print aa.weekday()

    print str(int(time.time() * 1000))
    t1 = time.time()
    print t1
    print time.ctime()
    #t = 1490060308998 * 1.00 / 1000
    t = 1503048528*1.00
    print time.ctime(t1)

    print time.ctime(t)
    t3 = time.ctime(t)

    print time.gmtime(t)
    #print time.strptime(t3,'%Y-%m-%d')
    print type(t3)


def format():
    print "*" * 10


def from_book():
    str1 = '2017/01/08'
    str2 = '20170108'
    date_type = datetime.datetime.strptime(str1, '%Y/%m/%d')
    date_type2 = datetime.datetime.strptime(str2, '%Y%m%d')
    print date_type2
    print type(date_type2)


#运行了多少时间
def time_run():
    start = datetime.datetime.now()
    print start
    time.sleep(3)

    end = datetime.datetime.now()
    print end
    print "time use ", (end - start).seconds
    print end.strftime("%H:%M:%S")


def time_fun():
    timestamp = 20170414
    #timestamp=long(1492744322234)
    datearr = datetime.datetime.utcfromtimestamp(timestamp)
    print datearr
    timestr = datearr.strftime("%Y-%m-%d %H:%M:%S")
    print timestr


#时间戳的使用

def time_exchange():
    str_time = '2017-04-21 11:12:02.234'
    print 'type of str_time ', type(str_time)
    #字符转为datatime类型
    locatime = datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S.%f')
    print locatime
    print 'type of locatime ', type(locatime)
    #datatime类型转为timestamp timestamp 为long类型
    t_stamp = long(time.mktime(locatime.timetuple()) * 1000.0 + locatime.microsecond / 1000.0)
    print t_stamp
    print 'type of t_stamp ', type(t_stamp)
    #timestamp类型转为 datatime
    d_time = datetime.datetime.fromtimestamp(t_stamp / 1000.0)
    print d_time

    current = datetime.datetime.now()
    print current
    #datatime转为str
    current_str = current.strftime('%Y/%m/%d %H,%M,%S')
    print current_str

    curr_stamp = time.time()
    print "current time stamp : ", curr_stamp
    curr_struct = time.localtime()
    print "current struct :", curr_struct

    curr_d = datetime.datetime.fromtimestamp(curr_stamp)
    print curr_d

    cti = time.ctime(curr_stamp)
    print type(cti)
    print cti
    #dd=datetime.datetime.strptime(cti,'%Y-%m-%d %H:%M:%S')
    #print dd


#把分钟秒的字符转为datetime
def str_time_hour():
    t = '2017-08-19 08:30:12'
    t0 = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
    print type(t0)
    print t0

def time_cuo():
    #10位
    print int(time.time())
    t = 1503048528
    t2=1503048528*1.00
    updateTime = 1500713681000/1000.00
    t3 = time.ctime(t)
    t4 = time.ctime(t2)

    print 't3',t3
    print 't4',t4
    curr_d = datetime.datetime.fromtimestamp(updateTime)
    print curr_d

def time_format():
    print type(time.strftime("%Y-%m-%d %H:%M:%S"))
    t=time.strftime("%Y-%m-%d %H:%M:%S")
    print t
    today=datetime.date.today()
    print today
    print type(today)



if __name__ == "__main__":
    #format()
    #from_book()
    #time_run()
    #test2()
    #time_fun()
    #time_exchange()
    #obj=DateTest3()
    #obj.getPreviousDay()
    #str_time_hour()
    #time_string_test()
    #time_cuo()
    time_format()