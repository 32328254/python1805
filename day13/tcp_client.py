#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
创建TCP客户端的步走著有如下：
1.创建客户端套接字:cs = cocket.socket()
2.尝试连接服务器:cd.connect()
3.与服务器通信:cs.send()/cs.recv()
4.关闭客户端套接字:cs.close()
"""
import socket

host = '127.0.0.1'
port = 12345
addr = (host, port)

c = socket.socket()  # 创建客户端套接字
c.connect(addr)  # 连接客户端
while True:
    data = input(">>>") + "\r\n"
    data = data.encode('utf8')
    c.send(data)  # 发生数据
    if data.strip() == b"quit":
        break
    print(c.recv(1024).decode('utf8'), end='')  # 接受数据
c.close()
