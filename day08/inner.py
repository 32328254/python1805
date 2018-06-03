#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def foo():
    print("is foo")
    def bar():
        print("is bar")
    bar() #调用bar

if __name__ == '__main__':
    foo()
