#socketsever.py
from socketserver import *

# class Server(ThreadingMixIn,TCPServer):
# class Server(ThreadingTCPServer,TCPServer):
class Server(ForkingTCPServer):
#     pass
    pass
# 创建多线程的TCP服务器
class Handler(StreamRequestHandler):
    def handle(self):
        print('conn_from',self.client_address)
        while True:
            #self.request 是客户端链接服务器的套接字
            data = self.request.recv(1024).decode()
            if not data:
                break
            print('recv message is ',data)
            self.request.send(b'recv your message')


server = Server(('127.0.0.1',8888),Handler)


server.serve_forever()
