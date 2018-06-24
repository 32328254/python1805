#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
统计每个客户端访问apache服务器次数
将统计信息通过字典显示出来
分别统计客户端是firefox和MSIE的访问次数
分别使用函数和类方式实现
127.0.0.1
"""
import re

count = {}
def count_info(fname,data):
    cpatt = re.compile(data)
    with open(fname,'r') as f:
        for info in f:
            result = cpatt.search(info)
            #print(result.group())
            if result:
                key = result.group()
                #print(key)
                count[key] =  count.get(key,0) + 1
    return count

if __name__ == '__main__':
    data = '^(\d+\.){3}\d+'
    name = 'access.log'
    result = count_info(name,data)
    print(result)
