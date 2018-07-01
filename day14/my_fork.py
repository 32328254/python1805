#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
fock编程基本思路
需要使用os模块
os.fock()函数实现forking功能.
python中,绝大多数的函数只返回一次,os.fock将返回两次，针对fock的调用,在父进程中返回子进程的PID,对于子进程,返回pid0
fock 是将父进程的资源copy一份生成子进程,然后子进程继续执行,等子进程执行完成后，父进程继续执行.
"""
# import os
# a = "hello"
# b = "你好"
# print(a)
# os.fork() #生成子进程
# print(b)


import os

print("staring...")
pid = os.fork()
print(pid)
if pid == 0:
    print("this is child")
else:
    print("this is father")
print("all")