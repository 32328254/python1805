#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session


session = Session()
#session.query(Departments).order_by(Departments.dep_id) #print sql
for instance in session.query(Departments).order_by(Departments.dep_id):
    print("dep_id is :%d,name is %s"%(instance.dep_id,instance.dep_name))

