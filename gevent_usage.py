from gevent import monkey;

monkey.patch_socket()
import gevent, requests


def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0.1)


def get_data(url):
    print gevent.getcurrent()
    resp = requests.get(url)
    print len(resp.text)


def testcase():
    print "Version: ", gevent.version_info
    gevent.joinall([gevent.spawn(get_data, 'https://python.org/'),
                    gevent.spawn(get_data, 'https://www.yahoo.com/'),
                    gevent.spawn(get_data, 'https://github.com/')])


def main():
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)
    g4 = gevent.spawn(f, 5)
    g5 = gevent.spawn(f, 5)
    g1.join()
    g2.join()
    g3.join()
    g4.join()
    g5.join()


# main()
testcase()
