#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import getpass

#接受用户输入
name = input("please input you name:")
passwd = input("plase input you password:")
#passwd = getpass.getpass('please input you password:')

#定义常量
name_ok = 'bob'
passwd_ok = '123456'

user_list = ['bob','alice','tom']

if name not in user_list:
    print(name + 'user not exits')

elif name == name_ok and passwd == passwd_ok:
    print('weclome ' + name + 'login success')
else:
    print('password error')
