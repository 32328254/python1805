#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#闭包

def counter(start=0):
    count = start
    def incr():
        nonlocal count  #流浪
        count += 1
        return count
    return incr

if __name__ == '__main__':
    a = counter()
    a()  #a()=incr()
    print(a())