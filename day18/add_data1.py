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
user1 = Employees(emp_id=1,
                  emp_name="zs",
                  gender='man',
                  birth_date='2018-07-14',
                  phone='12345678901',
                  email="2sd@qq.com",
                  dep_id=1)
user2 = Employees(emp_id=2,
                  emp_name="ls",
                  gender='man',
                  birth_date='2018-02-11',
                  phone='12345678902',
                  email="ls@qq.com",
                  dep_id=1)
user3 = Employees(emp_id=3,
                  emp_name="ww",
                  gender='man',
                  birth_date='2018-06-13',
                  phone='12345678901',
                  email="2sd@qq.com",
                  dep_id=2)
user4 = Employees(emp_id=4,
                  emp_name="zl",
                  gender='man',
                  birth_date='2018-04-14',
                  phone='12345678901',
                  email="2sd@qq.com",
                  dep_id=2)
session.add_all([user1,user2,user3,user4])
session.commit()
session.close()