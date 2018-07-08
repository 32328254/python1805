#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='tmooc',db='tedu',charset='utf8')
cursor = conn.cursor()
query1 = "select * from departments ORDER BY dep_id"
cursor.execute(query1) #执行
data1 = cursor.fetchone() #获取一行数据
data2 = cursor.fetchmany(2) #获取2行
result = cursor.fetchall()  #获取所有
print(data1)
print(data2)
print(result)
cursor.close()
conn.close()
for i in range(len(result)):
    print("de_id:%d,de_name:%s"%(result[i][0],result[i][1]))