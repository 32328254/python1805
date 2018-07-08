#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='tmooc', db='tedu', charset='utf8')
cursor = conn.cursor()
update1 = "UPDATE departments SET dep_name=%s WHERE dep_id=%s"
data = ("rz", 1)
cursor.execute(update1, data)
dels = "delete from departments where dep_name = %s"
cursor.execute(dels, ('sq1'))
conn.commit()
cursor.close()
conn.close()
