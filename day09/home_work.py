#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

count = 0


def nums():
    a = random.randint(1,100)
    b = random.randint(1,100)
    return a,b


def num_count(a,b):
    if a > b :
        c = a - b
    else:
        c = b - a
    print("c=%d"%c)
    return c


def user_input():
    try:
        choice_num = int(input("please input you choice:"))
    except:
        print('input ERROR:')
    return choice_num


def guess(comput,user):

    while count < 3:
        if comput != user:
            comput + 1


if __name__ == '__main__':
    a,b = nums()
    print("a=%d,b=%d"%(a,b))
    num_count(a,b)
