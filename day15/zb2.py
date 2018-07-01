#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
python 可以使用waitpid()来处理子进程
waitpid()接受两个参数,第一个参数设置为-1,表示与wait()函数相同,第二个参数如果设置为0表示挂起父进程,直到子进程退出,设置为1表示不挂起父进程.
waidpid()的返回值:如果子进程尚未结束则返回0,否则返回子进程PID

"""
import os
import time

print('Starting...')
pid = os.fork()
if pid:
    # print(os.waitpid(-1, 0))  # 挂起父进程，waitpid返回子进程pid
    time.sleep(7)
    print(os.waitpid(-1, 1))  # 第二个参数是1，表示不挂起父进程,第二个参数是0，表示挂起父进程
else:
    print('in child')
    time.sleep(5)
    print('child done')
