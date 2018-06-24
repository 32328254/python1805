#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
1.创建服务器套接字:s = socket.socket()
2.绑定服务器套接字:s.bind()
3.接收,发生数据:s.recvfrom()/s.sendto()
4.关闭套接字s.close()
"""
import socket
host = ''
port = 12345
addr = (host,port)
s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)

data , cli_addr = s.recvfrom(1024)
print(data)
s.sendto(b'server\r\n',cli_addr)
s.close()
