#!/usr/bin/env python3
# -*- coding:utf-8 -*-
file_name = '/tmp/mima'
binary_file = '/usr/bin/ls'
f = open(file_name,'r')
#data = f.readlines() #一次性读到list中,list中的每行是一个元素
#data = f.read()      #一次性读取文件中的全部内容
#date = f.readline()  #每次读取一行
data = f.read(4096)  #每次读4096字节(4KB)
data = f.writable()  #是否可读
print(data)
f.close()

f = open(binary_file,'rb')  #以二进制文件打开
data = f.read()
print(data)
f.close()
