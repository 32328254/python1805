
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from dbconn import Departments,Session,Employees
session = Session()
"""
大于：>
小于：<
"""
"""
相等
"""
qset = session.query(Employees).filter(Employees.dep_id==1).filter(Employees.gender=='男') #多filter查询,其实是sql中的and
print(qset)
for instance in qset:
    print(instance.emp_name)
session.close()

"""
不相等
"""
qset = session.query(Employees).filter(Employees.dep_id!=1).filter(Employees.gender!='男') #多filter查询,不等于
print(qset)
for instance in qset:
    print(instance.emp_name)
session.close()
"""
模糊查询
"""
qset = session.query(Employees).filter(Employees.dep_id!=1).filter(Employees.emp_name.like('%z%')) #多filter查询,模糊匹配
print(qset)
for instance in qset:
    print(instance.emp_name)
session.close()

