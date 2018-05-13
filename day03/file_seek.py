#!/usr/bin/env python3
# -*- coding:utf-8 -*-
f = open('/tmp/mima')
f.read(5) #读取5个字节,文件指针向后移动5个字节
f.tell()  #获取当前的文件指针