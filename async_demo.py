# -*-coding=utf-8-*-

# @Time : 2018/9/12 10:47
# @File : async_demo.py
import asyncio
import random
import time

import aiohttp


async def async_function():
    return 1

async def async_generator():
    yield 1


# print(type(async_function),type(async_generator))
# print(type(async_function()),type(async_generator()))
try:
    ret=async_function().send(None)
    print(ret)
except StopIteration as e:
    print(e)


class Potato(object):

    # def __init__(self,name):
    #     self.name=name
    #
    # def __repr__(self):
    #     return self.name

    @classmethod
    def make(cls,num,*args,**kwgs):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls,*args,**kwgs))

        return potatos

# p=Potato('google')
# print(p)

potatos = Potato.make(10)
print(len(potatos))
# for i in potatos:
    # print(i)



def ask_for_more():
    time.sleep(random.random())
    potatos.extend(Potato.make(random.randint(1,10)))

def take_potatos(num):
    count = 0
    while True:
        if len(potatos)==0:
            ask_for_more()
           # time.sleep(1)
        else:
            p=potatos.pop()
            yield p
            count+=1
            if count == num:

                break


#没有使用异步
def sync_mode():
    start=time.time()
    def buy_potato():
        buckets =[]
        for p in take_potatos(50):
            print(p)
            buckets.append(p)


    buy_potato()
    print('time used {}'.format(time.time()-start))


def async_mode():

    potatos = Potato.make(10)
    async def ask_for_more():
            # time.sleep(random.random())
            await asyncio.sleep(random.random())
            potatos.extend(Potato.make(random.randint(1, 10)))

    async def take_potatos_async(num):
        count = 0
        while True:
            if len(potatos) == 0:
                await ask_for_more()
            # time.sleep(1)

            p = potatos.pop()
            yield p
            count += 1
            if count == num:
                break

    async def buy_potato_async():
            buckets =[]
            async for p in take_potatos_async(50):
                # print(p)
                buckets.append(p)

    start = time.time()
    loop = asyncio.get_event_loop()

    loop.run_until_complete(buy_potato_async())
    # loop.run_until_complete(asyncio.wait([buy_potato_async(),buy_potato_async()]))
    loop.close()
    print('use time {}'.format(time.time()-start))


def class_async():
    class ThreeTwoOne:
        async def begin(self):
            print(3)
            await asyncio.sleep(1)
            print(2)
            await asyncio.sleep(1)
            print(1)
            await asyncio.sleep(1)
            return

    async def game():
        t = ThreeTwoOne()
        await t.begin()
        print('start')

    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([game(),game(),game()]))
    loop.close()
    # game()



def yield_from_demo():
    def sub_gen():
        yield 1
        yield 2
        yield 3
        yield 4

    def gen():
        return (yield from sub_gen())


    def main_app():
        for val in gen():
            print(val)

    main_app()

import types
# 使用语法测试
def use_keyword():

    @types.coroutine
    def compute(x,y):
        print('Compute {} + {} ...'.format(x,y))
        yield from asyncio.sleep(1.0)
        return x+y

    async def print_sum(x,y):
        result = await compute(x,y)
        print('{} + {} = {}'.format(x,y,result))

    loop =asyncio.get_event_loop()
    loop.run_until_complete(print_sum(9,9))
    loop.close()

def liaoxuefeng_async():
    async def hello():
        print('hello')
        await asyncio.sleep(1)
        print('hello again')

    loop =asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()

async def http_demo(url):
    # url = 'https://github.com'
    headers = {'User-Agent':'android 8'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            print(await resp.text())


async def http_

loop =asyncio.get_event_loop()
url_list = ['http://30daydo.com','https://github.com']
func_list = [http_demo(url) for url in url_list]
loop.run_until_complete(asyncio.wait(func_list))
loop.close()

# class_async()
# yield_from_demo()
# sync_mode()
# async_mode()
# use_keyword()
# liaoxuefeng_async()