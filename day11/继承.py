#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
当类之间有显著的不同，子类可以继承父类的所有,但子类还有自己的一些属性和方法

"""

class BearToy(object):
    def __init__(self,color,size):
        self.color = color
        self.size = size

    def speak(self):
        print("i can speak")

class NewBearToy(BearToy):  #继承父类BearToy

    def __init__(self,color,size,data):
        #BearToy.__init__(self,'red','small') #通过类的名字调用父类的初始化函数,不建议.

        super(NewBearToy,self).__init__(color,size)
        self.data = data
        #super(NewBearToy, self).__init__('red', 'big') #硬编码,不建议.

    def new_print(self):
        print(self.color,self.size)

    def speak(self):  #父子类中有相同的方法,会使用子类的方法
        print("this is 子类 方法")


if __name__ == '__main__':
    b = NewBearToy('green','big','2018-06-10')
    b.new_print()