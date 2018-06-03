#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def func(x):
    if x == 1:
        return x
    return x * func(x -  1)
         # 5 * func(5)
         # 5 * 4 * func(3)
         # 5 * 4 * 3 * func(2)
         # 5 * 4 * 3 * 2 * func(1)  #func(1) 返回自身
         # 5 * 4 * 3 * 2 * 1
if __name__ == '__main__':
    a = func(5)
    print(a)