#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
共有方法：fun()
私有方法：__fun(),开头双下划线
内置方法：__init__,

"""
class B:

    def __init__(self):  #内置方法，初始化变量,类实例化会自动被执行。
        print("这个自动执行")

    def fun1(self):  #共有方法
        print("this is opublic fun")

    def __fun2(self):  #私有方法
        print("this is privte fun")

    def fun3(self):
        self.__fun2()   #调用私有fun2,类内部调用

if __name__ == '__main__':
    b = B()
    #b.fun1()
    #b.fun2()  #不能在外部调用私有方法
    #b.fun3()