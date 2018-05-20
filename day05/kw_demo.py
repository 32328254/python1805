#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
程序接受用户输入,判断用户输入的标识符是否合法,用户输入的标识符不能使用关键字,有不合法字符,需要指明第几个不合法
"""
import keyword
import string

strings = string.ascii_letters + '_' #定义合法的首字符

def get_user(data):
    #data = input("please input you identifier:")
    if not keyword.iskeyword(data):  # 如果不是关键则进行字符合法判断
        if data[0] in strings:  # 判断首字符是否合法
            for k,v in enumerate(data[1:]):
                if v not in string.digits + strings:
                    print("number %d %s is invaild!" % (k+1, data[k+1])) #注意加一，因为是从第二个字符开始
                    #return ("number %d %s is invaild!" % (k+1, data[k+1]))
            print("%s is vaild"%data)
        else:
            print("the first number %d %s is invaild!" % (0, data[0]))  # 输出第一个字符不合法
    else:
        print(data + " is keyword")


if __name__ == '__main__':
    data = input("please input you identifier:")
    get_user(data)
