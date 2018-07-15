#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import namedtuple
from dbconn import Departments,Session
session = Session()
qset = session.query(Departments.dep_name).filter(Departments.dep_id==2) #过滤
for result in qset:
    print(result)
session.close()