#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def set_color(func):
    def red(*word): #拆包
        return "\033[31;1m%s\033[0m" % func(*word)   #拆包

    return red


@set_color
def hello():
    print("hello")


@set_color
def welcome(word):
    print("welcome %s"%word)


if __name__ == '__main__':
    hello()   #hello = set_color(hello)
    welcome('chine')
