#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
from sqlalchemy import and_,or_
session = Session()
qset = session.query(Departments.dep_name=='development')
print(qset)
print(qset.all())

q1 = session.query(Departments).filter(Departments.dep_name=='development')
print(q1)
for result in q1:
    print(result)

q1 = session.query(Departments).filter(Departments.dep_name=='development')
q1.update({Departments.dep_name:"开发部"})
session.commit()
session.close()



q1 = session.query(Departments).filter(Departments.dep_name=='开发部')
print(q1)
for result in q1:
    print(result)