#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def add(x,y):
    print(x +y)

if __name__ == '__main__':

    nums = [100,200]
    add(*nums)  #*nums表示把nums拆开


    ndict = {'x':100,'y':200}
    add(**ndict)  #**拆成x=100,y=200, 注意实参和形参要一至