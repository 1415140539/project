'''

frame
    run with  Thread
    conduct gongneng

'''

import socket
import sys
import os
import time
import threading
class Ch_Run():
    def __init__(self,conn):
        self.conn = conn
    def look(self,file_path):
        print('开始look功能')
        for i in os.listdir(file_path):
            self.conn.send(i.encode())
            time.sleep(0.1)
        self.conn.send(b'NO')
        print('look功能以实现')
    def quit(self):
        print('开始退出功能')
        self.conn.send('可惜我是多线程,没有这个功能'.encode())
        self.conn.send(b'F')
    def get(self,data):
        print('running get')
        file_name = data[1:].strip()
        path = os.getcwd()
        if file_name  in os.listdir(path):
            try:
                print(path + file_name)
                f = open(path +'\\'+ file_name ,'rt')
                print('successful')
                for i in f.readlines():
                    print(i)
                    self.conn.send(i.encode())
                self.conn.send(b'OK')
                f.close()
            except OSError:
                print('open file failed ' )
        else:
            self.conn.send(b'no')



def func(conn):
    ch = Ch_Run(conn)
    while True:
        time.sleep(0.1)
        data = conn.recv(1024).decode()

        if not data:
            break
        print('收到消息')
        if data == 'L':
            ch.look(FILE_PATH)
        elif data == 'Q':
            print('Q')
            ch.quit()
        elif data[0] == 'G':
            print('G')
            ch.get(data)
def main():


    HOST = '127.0.0.1'
    PORT = 8888
    ADDR = (HOST,PORT)
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    soc.bind(ADDR)
    soc.listen(5) # 设置监听模式

    while True:
        try:
            conn, addr = soc.accept()
        except KeyboardInterrupt:
            print('键盘退出')
            sys.exit(1)
        except Exception as err:
            print(err)
        print('开始线程')
        th = threading.Thread(target = func , args = (conn,))
        th.start()
        print('线程进行中')
if __name__ == '__main__':
    main()