from gevent import monkey
monkey.patch_all()
from gevent.server import StreamServer


def connection_handler(socket, address):
    for l in socket.makefile('r'):
        socket.sendall(l)


if __name__ == '__main__':
    server = StreamServer(('127.0.0.1', 8000), connection_handler)
    server.serve_forever()
