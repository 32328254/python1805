#!/usr/bin/env python3
# -*- coding:utf-8 -*-
py_str = 'python'
print(len(py_str))
py_str[0] #下标从0开始
py_str[5] #取最后一个值
py_str[-1] #从右向左取值
py_str[2:4] #切片,包含启始，不包含结尾
py_str[2:] #从下标2开始,到结尾
py_str[:2] #从开头取到2
py_str[::2] #从开头取到尾，步长为2
print(py_str[::2])
print(py_str[1::2]) #从第二个字符开始取值,步长为2
print(py_str[::-1]) #步长值为-1,表示从右向左取，【取反】
print(py_str[::-1][1::2]) #反向带步长取反

py_str + 'is cool' #字符串拼接
py_str * 2 #
