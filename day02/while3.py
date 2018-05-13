#!/usr/bin/env python3
# -*- coding:utf-8 -*-
sum100 = 0
counter = 0

while counter < 100:
    counter += 1
    #if counter %2 == 1: #判断 0 为假,非零为真,所以 == 1可以省罗
    if counter % 2:
        continue
    sum100 += counter
print(sum100)