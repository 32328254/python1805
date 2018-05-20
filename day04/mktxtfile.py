#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os


def get_fname():
    while True:
        fname = input("file name:")
        if not os.path.exists(fname):
            break
        print("file exits,please try age!!!")
    return fname


def get_content():
    content_info = []
    while True:
        line = input("exit to quit!>")
        if line == "exit":
            break
        content_info.append(line)
    return content_info


def wfile(fname, data):
    with open(fname, 'w') as fobj:
        fobj.writable(content_data)


if __name__ == '__main__':
    fname = get_fname()
    content_data = get_content()
    content_data = ['%s\n' % line for line in content_data]  # 列表表达式
    wfile(fname, content_data)
