#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
from sqlalchemy import and_,or_
session = Session()

qset = session.query(Employees).filter(and_(Employees.dep_id==2,Employees.gender=='男')) #and
qset = session.query(Employees).filter(or_(Employees.dep_id==2,Employees.dep_id==1))     #or
qsets = session.query(Employees.emp_name).filter(and_(Employees.emp_name=='zl',Employees.gender=='man'))     #or
print(qset)
for instance in qset:
    print(instance.emp_name)
print(qset.all()) #返回所有满足条件的结果
print(qset.first()) #返回满足条件的第一个值
print(qsets.one()) #取出所有结果,如果有多个结果则抛出异常
print(qsets.scalar()) #调用one(),返回第一列的结果