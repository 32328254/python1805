#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
python 允许重继承,即一个类可以是多个父类的子类，子类可以拥有多有父类的属性
继承的顺序是从左到右,从下到上
"""


class A:
    def foo(self):
        print("this is A ")
    def bar(self):
        print("in A bar")

class B(A):              #继承A
    def foo(self):
        print("this is B")

class C:
    def foo(self):
        print("this is C")

class D(C,B):
    pass

if __name__ == '__main__':
    a = D()
    a.foo()
    a.bar()