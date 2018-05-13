#!/usr/bin/env python3
# -*- coding:utf-8 -*-
file_name = '/tmp/mima'
f = open(file_name,'r')
for line in f:
    print(line,end='')
f.close()