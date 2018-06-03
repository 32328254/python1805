#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from time import sleep,time

def deco(func):

    def timeit():  #高阶函数,func--->loop
        start = time()
        result = func()   #func --->loop
        end = time()
        return result,end -start
    return timeit
@deco
def loop():
    alist = []
    for i in range(1,11):
        alist.append(i)
        sleep(0.2)
    return alist

if __name__ == '__main__':
    #print(timeit(loop))
    #loop = deco(loop)  #新的 loop是timeit  等于@deco
    print(loop())
