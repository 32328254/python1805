#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
from sqlalchemy import and_,or_
session = Session()
finance = session.query(Departments).get(3)
qset = session.query(Departments).filter(Departments.dep_name=="财务部门")
result = qset.all()[0]
result = qset.one()
result = qset.first()
result = finance
print(result)
session.delete(result)
session.commit()
session.close()