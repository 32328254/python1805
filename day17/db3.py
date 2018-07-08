#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
移动游标
如果希望不是从头取数据,可以先移动游标
cur.scroll(1,mode="relative") #从当前游标开始移动
cur.scroll(2,mode="absolute") #从绝对路径开始移动
"""

import pymysql


conn = pymysql.connect(host='localhost',port=3306,user='root',password='tmooc',db='tedu',charset='utf8')
cursor = conn.cursor()
query1 = "select * from departments ORDER BY dep_id"
cursor.execute(query1) #执行
cursor.scroll(3,mode='relative') #当前为值移游标
result = cursor.fetchone() #获取一个值
print(result)
cursor.scroll(3,mode='absolute') #从绝对为值移动游标
result1 = cursor.fetchone()  #获取一个值
print(result1)
cursor.scroll(-1,mode='relative') #向上移动游标
result2 = cursor.fetchone()
print(result2)
cursor.close()
conn.close()
