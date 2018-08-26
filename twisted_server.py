from twisted.internet import protocol, reactor
from time import ctime

PORT = 10001


class TSServerProtocol(protocol.Protocol):

    def connectionMade(self):
        client = self.client = self.transport.getPeer().host
        print(client)
        print('等待连接，来自：', client)

    def dataReceived(self, data):
        data = data.decode()
        print('收到的内容：', data)
        self.transport.write(('[%s] %s' % (ctime(), data)).encode())


factory = protocol.Factory()
factory.protocol = TSServerProtocol
print('等待连接：')
reactor.listenTCP(PORT, factory)
reactor.run()
