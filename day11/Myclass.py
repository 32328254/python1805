#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
类:用来描述具有相同的属性和方法的对象的集合,它定义了该集合中每个对象所共有的属性和方法,对象就是类的实例
实例化:创建一个类的实例,类的具体对象
方法：类中定义的函数
对象:通过类定义的数据结构实例,对象包括两个数据成员,类变量和方法
"""
"""
共有属性：类里面,方法外面,类的外部内部都可以调用,可以使用对象和类名字调用
私有属性：__size #属性前有两个下划线,类的内部可以调用(self.__size),外部不可以调用
内置属性：__dict__  #前后双下划线为内置属性.
"""

"""
对象属性：方法内部定义
"""

class A:                  #定一个类
    color = 'red'         #类属性,公有属性
    __size = 'small'      #私有属性
    #__dict__ = 'sss'      #内置属性

    def fun(self):        #类方法
        print(self)       #self表示实例化本身
        print("this is method")

    def fun1(self):
        self.name = self  #对象属性
        print(self.name)

    def fun2(self):
        print(self.name) #可以直接使用fun1的name

if __name__ == '__main__':
    a = A()               #类的实例化,a是实例或者叫对象
    #print(a.color)        #对象调用属性color
    #print(a.fun())        #对象调用方法fun
    print(a.fun1())
    print(a.name)
