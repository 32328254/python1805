#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

def get_filename():
    while True:
        file_name = input('please input you file name: ')
        if not os.path.exists(file_name):
            return file_name
            break
        else:
            print(file_name,"exits,please input age!!!")
if __name__ == '__main__':
    a = get_filename()
    print(a)
