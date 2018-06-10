#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Manufacture(object):
    def __init__(self,telnet,addr):
        self.telnet = telnet
        self.addr = addr


class BearToy(object):
    def __init__(self, color, size,tel,addr):  # 构造器,当类被实例化时自动执行
        self.color = color
        self.size = size
        self.factory = Manufacture(tel,addr)  #类组合

    def __str__(self):
        return "this is BearToy instance"

    def sing(self, song):
        print("%s color is %s,size is %s,and I can %s" % (self.color,self.color, self.size, song))




if __name__ == '__main__':
    #tidy = BearToy('red', '5')  #实例化并给构造器传参
    #tidy.sing('haha')           #调用方法
    #print(tidy)                 #__str__的返回值
    bear1 = BearToy('orange','small','123','beijing')
    print(bear1.sing("xixi"))
    print(bear1.factory.addr) #调用组合类