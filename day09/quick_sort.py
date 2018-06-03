#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from random import randint
def qsort(data):
    if len(data) < 2:  #如果列表中的元素只有一个或者是0个就返回
        return data
    middle = data[0]  #取列表中的第一个值当做中间值
    smaller = []
    larger = []
    for i in data[1:]: #从列表中的第二个元素以次取出
        if i < middle:
            smaller.append(i)
        else:
            larger.append(i)
    return qsort(smaller) + [middle] + qsort(larger)


# smaller + [middle] + larger


if __name__ == '__main__':
    reslut = qsort([randint(1,100) for i in range(10)])
    #a = qsort([1,2,5,3,2,5,7,8,4,6,0])
    print(reslut)