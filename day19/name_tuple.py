#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import namedtuple
from dbconn import Departments,Session
"""
命名元组
"""
# students = namedtuple('students',['name','age','gender']) #第一个students和第二个students名字要相同
# zhangsan = students('zhangsan',25,'male')
session = Session()
qset = session.query(Departments,Departments.dep_name)[1:3]
print(qset) #

for row in qset:
    print(row)
    print(row.Departments,row.dep_name)


