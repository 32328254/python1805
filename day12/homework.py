#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
服务器监听在0.0.0.0的21567端口上
收到客户端数据后，将其加上时间崔后回复给客户端
如果客户端发过来的字符全是空白字符,则终止与客户端的连接
"""
import socket
import time
host = ""
port = 21567
addr = (host,port)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)
while True:
    client, address = s.accept()
    print("client ip address is ",address)
    while True:
        info = client.recv(1024)
        print("client send info is ",info)
        if info.strip() != b"quit":
            date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            client.send("[%s] %s"%(date,info))
        else:
            client.close()
            break
    #client.close()
s.close()

