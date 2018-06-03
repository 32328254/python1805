#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
偏函数


"""
from functools import partial

def add(x,y,z):
    return x + y + z

if __name__ == '__main__':
    add(10,20,5)
    add(10,20,10)
    new_add = partial(add,10,20) #固定参数
    new_add(3)