import socket
import time,os

def  lst():
    print('LOOK'.center(20,"*"))
    print('GET'.center(20, "*"))
    print('PUT'.center(20, "*"))
    print('QUIT'.center(20, "*"))
class Ch_func():
    def __init__(self,soc):
        self.soc =  soc
    def look(self):
        self.soc.send(b'L')
        while True:
            data = self.soc.recv(1204).decode()
            if data == 'NO':
                break
            print(data)
    def quit(self):
        print('开始退出')
        self.soc.send(b'Q')
        while True:
            data = soc.recv(1024).decode()
            if data == 'F':
                print('退出')
                break
            print(data)
    def get(self):
        print('start recv file ')
        path = os.getcwd()
        file = input('please file name')
        self.soc.send(('G  '+ file).encode())
        try:
            f1 = open(path+'\\'+'1'+file, 'wt')
            while True:
                data = self.soc.recv(1024).decode()
                print(data)
                if data == 'OK' or 'no':
                    print('exit')
                    break
                f1.write(data)
                time.sleep(0.1)
            f1.close()
        except OSError:
            print('open file failed')
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    soc.connect(ADDR)
    print('链接成功')
    ch = Ch_func(soc)
except Exception as err:
    print('错误是:',err)
while True:
    lst()
    data = input('请输入你的选择')
    if not data :
        print('已经退出')
        break
    elif data == 'L':
        ch.look()
    elif data == 'Q':
        ch.quit()
    elif data == 'G':
        ch.get()
    input('按回车继续')