#!/usr/bin/env python3
# -*- coding:utf-8 -*-
file_name = '/tmp/mima'
with open(file_name,'r') as f: #with语句将会在代码块中执行完毕后自动关闭文件
    print(f.readline())