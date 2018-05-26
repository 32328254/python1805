#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import sys
"""
import time
#alist = ['*'] * 20
#print(alist)

# for i in range(20):
#     alist[i] = '@'
#     print("\r%s" %alist,end='')
#     time.sleep(1)
"""
#单次打印
# l = 19
# print('#' * 20,end='')
# sys.stdout.flush() #标准输出有缓存,flush可以立即输出到屏幕
# for i in range(20):
#     time.sleep(1)
#     print('\r%s@%s'%('#' * i,'#' * (l -i)),end='')
l = 19
print('#' * 20,end='')
sys.stdout.flush()
i = 0
while True:
    time.sleep(1)
    print('\r%s@%s'%('#' * i,'#' * (l -i)),end='')
    if i == l:
        i = 0
    i += 1