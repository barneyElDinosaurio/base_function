__author__ = 'xda'
import socket

data = b'GET /get HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nUser-Agent: python-socket\r\n\r\n'
url = 'httpbin.org'
s = socket.socket()
s.connect((url, 80))
s.sendall(data)
print(s.recv(999))

