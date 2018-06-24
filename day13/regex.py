#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
print(re.match('foo','food')) #从开头开始匹配
print(re.match('foo','seafood')) #没匹配到,因为match是从头开始
m = re.match('f..','food')
print(m.group()) #m.group 取出匹配内容
m = re.search('f..','seafood') #search可以在任意位置匹配
print(m.group())
m = re.findall('f..','seafood') #匹配所有,返回一个列表
print(m)
result = re.finditer('f..','seafood') #匹配对象,然后for取值
for m in result:
    print(m.group())
cpatt = re.compile('f..')
m = cpatt.search('fxxxx')
print(m.group())

re.split('-|\.','hello-world.tar.gz') #用.和-切割
re.sub('x','y','ssxxcc') #把x替换成y
