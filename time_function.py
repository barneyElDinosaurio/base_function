# -*-coding=utf-8-*-
#日期函数的使用
import time, datetime


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
        last = now + datetime.timedelta(days=-3)
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


def format():
    print "*" * 10


def from_book():
    str1 = '2017/01/08'
    date_type = datetime.datetime.strptime(str1, '%Y/%m/%d')
    print date_type


if __name__ == "__main__":
    format()
    from_book()

