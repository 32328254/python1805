#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
服务器监听在0.0.0.0的12345端口上
收到客户端数据后，将其加上时间崔后回复给客户端
如果客户端发过来的字符全是空白字符,则终止与客户端的连接
"""
import socket
import time
import os

class TcpTimeServ(object):

    def __init__(self,host='',port=12345):
        self.addr = (host,port)
        self.serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def handle(self,data):
        while True:
            info = data.recv(1024)
            print("client send info is ", info)
            if info.strip() != b"quit":
                date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                data.send("[%s] %s" % (date, info))
            else:
                data.close()
                break

    def mainloop(self):
        try:
            while True:
                client, address = self.serv.accept()
                print("client ip address is ", address)
                status = os.fork()
                if status:
                    client.close()
                    while True:
                        result = os.waitpid(-1,1)  #优先处理僵尸进程
                        if result[0] == 0:
                            break
                else:
                    self.serv.close()
                    self.handle(client)
                    exit()

        except KeyboardInterrupt:
            print("server Ctrl C ")

if __name__ == '__main__':
        s = TcpTimeServ()
        s.mainloop()
