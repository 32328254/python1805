#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
静态方法
"""

class A:
    @classmethod
    def foo(cls):         #类方法
        print("cls--->",cls)
        print("this is A ")
    @staticmethod         #静态方法
    def bar():            #没有参数,是一个函数
        print("in A bar")
        A.foo()

if __name__ == '__main__':
    A.bar()