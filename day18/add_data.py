#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees,Salary


session = Session() #创建session会话
# dev = Departments(dep_name='development')
# print(dev.dep_name)
# print(dev.dep_id)
# dev = Departments(dep_name="人事部",dep_id=2)
# session.add(dev) #添加一个
ops = Departments(dep_name="运维部")
finance = Departments(dep_name="财务部")

session.add_all([ops,finance]) #添加多个
session.commit()
#print(dev.dep_id)
session.close()
