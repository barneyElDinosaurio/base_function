# -*-coding=utf-8-*-
import execjs
ctx=execjs.compile(open('person.js').read())
ctx.eval()