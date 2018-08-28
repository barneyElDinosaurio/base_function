from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 10001


class TSClientProtocol(protocol.Protocol):

    def sendData(self):
        data = input('>')
        print('print data')
        if data:
            print('正在发送', data)
            self.transport.write(data.encode())

        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode())
        self.sendData()


class TSClientFactory(protocol.ClientFactory):
    protocol = TSClientProtocol


reactor.connectTCP(HOST, PORT, TSClientFactory())
reactor.run()
