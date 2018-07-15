#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
from sqlalchemy import and_,or_
session = Session()
hr = session.query(Departments).get(3) #get用于查询主建为3的对象
print(hr)
hr.dep_name = "财务部门"
session.commit()
session.close()