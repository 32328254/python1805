#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
from sqlalchemy import and_,or_
session = Session()

sqet = session.query(Departments).count() #查询表中有多少条数据
print(sqet)