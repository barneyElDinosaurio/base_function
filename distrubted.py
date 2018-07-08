#-*-coding=utf-8-*-
#import requests
import time

from rq import Queue
from redis import Redis
from count_function import count_words


#print(count_words('http://nvie.com'))

'''
def main():
    redis_conn=Redis()
    q=Queue(connection=redis_conn)
    job=q.enqueue(count_words,'http://nvie.com')
    print(job.result)

    time.sleep(5)
    print(job.result)
'''
host_ip="10.19.133.255"
#redis_conn=Redis(host='192.168.2.234',port=6379,socket_connect_timeout=5)
redis_conn=Redis(host=host_ip,port=6379)
q=Queue(connection=redis_conn)
job=q.enqueue(count_words,'http://nvie.com')
print(job.result)

time.sleep(5)
print(job.result)




'''
if __name__ == '__main__':
    main()
'''