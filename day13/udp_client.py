#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
1.创建服务器套接字:s = socket.socket()
2.接收,发生数据:s.recvfrom()/s.sendto()
3.关闭套接字s.close()
"""
import socket
host = '127.0.0.1'
port = 12345
addr = (host,port)
c = socket.socket(type=socket.SOCK_DGRAM)
c.sendto(b'client',addr)
print(c.recvfrom(1024))
c.close()