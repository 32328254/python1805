#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day


    @classmethod    #类装饰器
    def create_date(cls,string_date):  #cls表示类
        y,m,d = map(int,string_date.split('-'))
        instance = cls(y,m,d)  #调用Date类
        return instance

    @staticmethod  #静态方法
    def is_date_valid(string_data):
        y,m,d = map(int,string_data.split('-'))
        return y < 9999 and  1<= m <= 12 and 1<= d <= 31 #返回true,false

if __name__ == '__main__':
    dt2 = Date.create_date('2018-06-22')
    print(dt2)
    print(Date.is_date_valid('2018-06-23'))