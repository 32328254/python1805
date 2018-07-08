#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
import datetime

conn = pymysql.connect(host='localhost',port=3306,user='root',password='tmooc',db='tedu',charset='utf8')
cursor = conn.cursor()
sql1 = "insert into employees(emp_id,emp_name,gender,brith_date,phone,email,dep_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
data = (1,'xx','male',datetime.datetime.now().strftime('%Y-%m-%d'),'11111111111','as@qq.com',1)
cursor.execute(sql1,data)
conn.commit()
cursor.close()
conn.close()