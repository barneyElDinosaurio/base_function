# # -*-coding=utf-8-*-
# # @Time : 2018/8/20 17:04
# # @File : treq_pressure.py

# from twisted.internet import epollreactor
# epollreactor.install()

from twisted.internet import reactor, task
from twisted.web.client import HTTPConnectionPool
import treq
import random
from datetime import datetime
from twisted.internet.task import react

# req_generated = 0
# req_made = 0
# req_done = 0

# cooperator = task.Cooperator()
#
# pool = HTTPConnectionPool(reactor)
#
#
# # 循环1s执行自己
# def counter():
#     '''This function gets called once a second and prints the progress at one
#     second intervals.
#     '''
#     global req_generated
#     global req_made
#     global req_done
#     print("Requests: {} generated; {}made; {}done".format(req_generated, req_made, req_done))
#     # reset the counters and reschedule ourselves
#     req_generated = req_made = req_done = 0
#     reactor.callLater(1, counter)
#
#
# def body_received(body):
#     global req_done
#     req_done += 1
#
#
# def request_done(response):
#     global req_made
#     deferred = treq.json_content(response)
#     req_made += 1
#     deferred.addCallback(body_received)
#     deferred.addErrback(lambda x: None)  # ignore errors
#     return deferred
#
#
# def request():
#     deferred = treq.post('http://api.host/v2/loadtest/messages',
#                          auth=('api', 'api-key'),
#                          data={'from': 'Loadtest &lt;test@example.com&gt;',
#                                'to': 'to@example.org',
#                                'subject':'test'},pool = pool)
#     deferred.addCallback(request_done)
#     return deferred
#
#
# def requests_generator():
#     global req_generated
#     while True:
#         deferred = request()
#         req_generated += 1
#         # do not yield deferred here so cooperator won't pause until
#         # response is received
#         yield None
#
#
# if __name__ == '__main__':
#     # make cooperator work on spawning requests
#     cooperator.cooperate(requests_generator())
#
#     # run the counter that will be reporting sending speed once a second
#     reactor.callLater(1, counter)
#
#     # run the reactor
#     reactor.run()

# from treq import get
#
# def done(response):
#     print(response.code)
#     # reactor.stop()
#     print('See you ?')
#
# def print_func():
#     print('ON print function')
#
# get("http://www.30daydo.com").addCallback(done)
# get("http://www.30daydo.com").addCallback(print_func)
#
# from twisted.internet import reactor
# reactor.run()
# print('end of program')
# reactor.stop()

# def print_response(response):
#     print(response.code)
#
# def main(reactor, *args):
#     d = treq.get('http://httpbin.org/get')
#     d.addCallback(print_response)
#     return d

# working
# from __future__ import print_function
def print_response(response):
    print(response.code, response.phrase)
    print(response.headers)

    return treq.text_content(response).addCallback(print)

def main(reactor, *args):
    d = treq.get('http://httpbin.org/get')
    d.addCallback(print_response)
    return d

react(main, [])



# working
# def download_file(reactor, url, destination_filename):
#     destination = open(destination_filename, 'wb')
#     d = treq.get(url)
#     d.addCallback(treq.collect, destination.write)
#     d.addBoth(lambda _: destination.close())
#     return d
#
# react(download_file, ['http://httpbin.org/get', 'download.txt'])