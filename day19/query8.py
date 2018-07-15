#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
session = Session()
qset = session.query(Employees).filter(Employees.dep_id.in_([1,2])) #in过滤
qset = session.query(Employees).filter(~Employees.dep_id.in_([1,2])) #not in过滤(区反)
qset = session.query(Employees).filter(Employees.dep_id.is_(None)) #is_(None)取空
qset = session.query(Employees).filter(Employees.dep_id.isnot_(None)) #isnot 取非空

print(qset)
