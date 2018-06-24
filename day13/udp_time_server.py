#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
from time import strftime

class UdpTimeServer(object):

    def __init__(self,host='127.0.0.1',port=12345):
        self.addr = (host,port)
        self.serv = socket.socket(type=socket.SOCK_DGRAM)
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)

    def mainloop(self):
        while True:
            data,cli_addr = self.serv.recvfrom(1024)
            data = '[%s] %s'%(strftime('%Y-%m-%d %H:%M:%s'),data.decode('utf8'))
            data = data.encode('utf8')
            self.serv.sendto(data,cli_addr)
if __name__ == '__main__':
    udp_serv = UdpTimeServer()
    udp_serv.mainloop()