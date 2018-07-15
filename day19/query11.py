#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
from sqlalchemy import and_,or_
session = Session()
qset = session.query(Employees.emp_name,Departments.dep_name).join(Departments,Employees.dep_id==Departments.dep_id) #多表查询,join()
print(qset)
print(qset.all())