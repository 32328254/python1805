#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
width = 50
list = ['xxxx','dfdd','sdsdfs']
print('*' * width)
for i in list:
    print('*%s*' % i.center(width - 2))
print('*' * width)
