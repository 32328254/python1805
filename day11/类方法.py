#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
类方法
"""

class A:
    @classmethod            #装饰器
    def foo(cls):           #cls是类名
        print("cls--->",cls)
        print("this is A ")
    def bar(self):
        print("in A bar")
        A.foo()            #直接在类内部通过类名调用foo

if __name__ == '__main__':
    #A.foo()  #可以通过类名调用
    #A.bar()
    a = A()
    a.bar()