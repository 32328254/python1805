#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
创建TCP服务器的主要步骤:
1.创建服务器套接字:s = socket.socket()
2.绑定地址到套接字:s.bind()
3.启动监听:s.listen()
4.接受客户端连接:s.accept()
5.与客户端通信:recv()/send()
6.关闭套接字:s.close()
"""


import socket
host = ''  #表示本机所有IP
port = 12345 #端口号,应该大于1024
addr = (host,port)
#创建一个TCP的网络套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置服务器在停止后,可以立即启动,地址默认保留60s
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr) #为套接字绑定地址
s.listen(1) #启动监听
cli_sock,cli_addr = s.accept() #accept返回客户端套接字和地址
print("client connected from:",cli_addr)
data = cli_sock.recv(1024) #接受客户端数据,最多1024字节
print(data)
if data == " ":
    cli_sock.close()  #关闭客户端
    s.close()  #关闭服务端
cli_sock.send(b'how are you\r\n') #发生数据