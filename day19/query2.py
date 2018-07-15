#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
session = Session()
qset = session.query(Employees.emp_name,Employees.phone)
for result in qset: #yuanzhu
    print(result)

for name,phone in qset:
    print("%s,%s"%(name,phone))