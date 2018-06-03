#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
def mygen():
    yield 10
    a = 10 + 20
    yield a
    yield "hello world"

if __name__ == '__main__':
    a = mygen()
    for i in a:
        print(i)
        time.sleep(0.5)