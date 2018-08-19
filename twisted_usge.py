# -*-coding=utf-8-*-
# @Time : 2018/8/19 22:41
# @File : twisted_usge.py
import time
from twisted.internet import reactor,defer,task


def schedule_install(customer):
    def schedule_install_wordpress():
        def on_done():
            print('Callback: finished installation for {}'.format(customer))

        print('Scheduling: installation for {}'.format(customer))
        return task.deferLater(reactor, 3, on_done)

    def all_done(_):
        print('all done for {}'.format(customer))

    d = schedule_install_wordpress()
    d.addCallback(all_done)
    return d

def twisted_develop_day(customers):
    print('Goodmorning from twisted developer')
    work = [schedule_install(customer) for customer in customers]
    join = defer.DeferredList(work)
    join.addCallback(lambda _: reactor.stop())
    print('Bye from twisterd developers')

start=time.time()
twisted_develop_day(["customer %02d" %i for i in range(15)])
reactor.run()
print('time used {}'.format(time.time()-start))