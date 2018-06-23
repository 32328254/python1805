#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
魔法方法
"""

class Book(object):

    def __init__(self,name,author):  #实例化时自己执行
        self.name = name
        self.author = author

    def __str__(self):  #返回字符串
        return "%s"%(self.name)

    def __call__(self):
        print("%s is written by %s"%(self.name,self.author))


if __name__ == '__main__':
    pybook = Book('core python','wesley') #调用__init__方法
    print(pybook)         #调用__str__方法
    pybook()              #调用__call__方法

