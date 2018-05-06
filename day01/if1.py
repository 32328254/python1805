#!/usr/bin/env python3
# -*- coding:utf-8 -*-
if 3 > 0:
    print('yes')

if 3 > 10:
    print('yes')

else:
    print('no')

if -0.0:  #不输出,任何值为0的数字都是False
    print('ok')

if 10: #输出
    print('10 ok')

if ' ': #任何非空对象都是True,空对象是False
    print('space ok')

if [10,20]: #输出
    print('list ok')