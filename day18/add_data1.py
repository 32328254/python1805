#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(20))
    gender = Column(String(20))
    birth_date = Column(Date)
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer,ForeignKey("departments.dep_id"))
"""
import time
from dbconn import Departments,Session,Employees,Salary

t = time.strftime("%Y-%m-%d",time.localtime())



session = Session()
user1 = Employees(emp_id=1,emp_name="zs",gender='man',brith_date='2018-07-14',phone='12345678901',email="2sd@qq.com",dep_id=1)
session.add_all()
session.commit()
session.close()