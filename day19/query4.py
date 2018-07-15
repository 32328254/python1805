#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session
session = Session()
qset = session.query(Departments.dep_name.label('部门')) #改名
for row in qset:
    print(row.部门)
session.close()
