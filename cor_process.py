import time
import asyncio
# 协程
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return

        print('[Consumer] consuming %s ...' % n)
        time.sleep(2)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[Productor] Producing %s ...' % n)
        r = c.send(n)
        print('[Productor] Consumer return %s' % r)


async def func(name):
    print('starting {} >>>>>'.format(name))

    if '百度' in name:
        print('延迟 1秒')
        await asyncio.sleep(1)
    if '谷歌' in name:
        print('延迟 3秒')
        await asyncio.sleep(3)

    if '腾讯' in name:
        print('延迟 5秒')
        await asyncio.sleep(5)
    print('Done of function {}'.format(name))

def first_demo():
    c = consumer()
    produce(c)

def second_demo():
    loop = asyncio.get_event_loop()

    name_list = ['腾讯','谷歌','百度']
    task_list = [func(i) for i in name_list]
    loop.run_until_complete(asyncio.wait(task_list))

def cor1():
    print('c1 start')
    yield
    print("in cor1-1")
    print("in cor1-2")
    print("in cor1-3")
    print('c1 end')

def cor2():
    print('c2 start')
    yield
    print("in cor2-1")
    print("in cor2-2")
    print("in cor2-3")
    print('c2 end')

def run(coros):
    ret = list(coros)

def third_demo():
    c1=cor1()
    c2=cor2()
    print(c1,c2)
    try:
        c1.send(None)
    except:
        pass
    try:
        c2.send(None)
    except:
        pass

def main():
    # first_demo()
    # second_demo()
    third_demo()

main()
