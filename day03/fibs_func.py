#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def gen_fib(len):
    list = [0,1]

    #len = int(input('length:'))
    for i in  range(len - 2):
        #num1 = list[-1]
        #num2 = list[-2]
        #sum = num1 + num2
        #list.append(sum)
        list.append(list[-1] + list[-2])
    #print(list)
    return list
if __name__ == '__main__':
    len = int(input('length:'))
    value = gen_fib(len)
    print(value)