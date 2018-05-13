#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""菲薄纳妾数列"""
list = [0,1]

len = int(input('length:'))
for i in  range(len - 2):
    #num1 = list[-1]
    #num2 = list[-2]
    #sum = num1 + num2
    #list.append(sum)
    list.append(list[-1] + list[-2])
print(list)

