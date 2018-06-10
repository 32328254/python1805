#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
类组合
"""

class Manufacture(object):
    def __init__(self,telnet,addr):
        self.telnet = telnet
        self.addr = addr

    def get_info(self):
        print(self.telnet,self.addr)

class BearToy(object):
    def __init__(self, color, size,tel,addr):  # 构造器,当类被实例化时自动执行
        self.color = color
        self.size = size
        self.factory = Manufacture(tel,addr)  #类组合

    def __str__(self):   #一般用于告诉用户这个类的功能
        return "this is BearToy instance"

    def sing(self, song):
        print("%s color is %s,size is %s,and I can %s" % (self.color,self.color, self.size, song))




if __name__ == '__main__':
    bear1 = BearToy('orange','small','123','beijing')
    print(bear1.sing("xixi"))
    print(bear1.factory.addr) #调用组合类
    bear1.factory.get_info()