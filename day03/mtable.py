#!/usr/bin/env python3
# -*- coding:utf-8 -*-
for i in range(1,10):
    #print(i)
    for j in range(1,i + 1):
        #print(j,"*",i,"=",i*j," ",end='')
        print("%d*%d=%d"%(j,i,j*i),end=' ')
    print()