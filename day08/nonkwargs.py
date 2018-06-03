#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def funx(*args):  #*号表示args是元组
    print(args)


def funx2(**kw_args):  #**表示kw_ages是个字典
    print(kw_args)


if __name__ == '__main__':
    funx()
    funx('xx')
    funx('xxx','www')
    funx('s','df','tr')
    funx2()
    funx2(name='zz')
    funx2(name='zz',age=25)
