#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from random import randint
def func2(x):
    return (x - 10) * 2

if __name__ == '__main__':
    nums = [randint(1,100)for i in range(10)]
    print(list(map(func2,nums)))
    print(list(map(lambda x:(x-10)*2,nums))) #返回列表