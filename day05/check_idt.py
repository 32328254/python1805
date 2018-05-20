#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
程序接受用户输入,判断用户输入的标识符是否合法,用户输入的标识符不能使用关键字,有不合法字符,需要指明第几个不合法
"""
import string
import keyword
first_chs = string.ascii_letters + '_'

def check_idt(data):
    alist = []
    if keyword.iskeyword(data):
        return ("%s is keyword"%(data) )
    if data[0] in first_chs:
        alist.append(0)
        return ("fist number is invalid")
    for k,v in enumerate(data[1:]):
        if v not in first_chs + string.digits:
            alist.append(k)
            return ("%d %s"%(k+2,data[k+2]))
    return ("%s is vlid"%(data))
    print(alist) #return了 所以取不到数据

if __name__ == '__main__':
    data = input("please input you identifier:")
    check_idt(data)