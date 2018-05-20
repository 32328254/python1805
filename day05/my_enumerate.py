#!/usr/bin/env python3
# -*- coding:utf-8 -*-


alist = ['bob','alice','tom',10,20,[1,2,3]]

for k,v  in enumerate(alist):
    print(k,v)

for k in enumerate(alist):
    print(k[0],k[1])

for ind in range(len(alist)):
    print(ind,ind[ind])
