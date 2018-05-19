#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
默认生成8位密码,
支持用户自定义输入密码长度
"""
import random
#from random import choice
import string

all_chs = string.ascii_letters + string.digits #大小写字母和数字

def get_password(length=8):
    result = ''
    for i in range(length):
        choice = random.choice(all_chs)
        result += choice
    #pd = ''.join(password)  #列表转字符串
    print(result)
    return result

if __name__ == '__main__':
    length = int(input("please input you length: "))
    get_password(length)
