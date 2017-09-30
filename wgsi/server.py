# -*-coding=utf-8-*-
from first import application
from wsgiref.simple_server import  make_server

httpd = make_server('',8080,application)
print 'Server HTTP on port 8080....'

httpd.serve_forever()