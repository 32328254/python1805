#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
DDL:数据库定义语言;如何创建数据库
DCL:数据库控制语言;如何授权语句
DML:数据库操作语言,如何增删改查
DQL:数据库查询语言,select语句
"""
"""
pip3 install pymysql #python 3版本
pip install mysql-python #python 2版本
连接数据库：
1.创建连接是访问数据库的第一步
conn = pymysql.connent(host='localhost',port=3306,user='root',password='tmocc',db='tedu',charset='utf8')
2.游标
游标(cursor)就是游动的标识,通俗的说，一条sql取出对应n条结果资源的接口/句柄就是游标,沿着游标可以一次取出一行
cursor = conn.cursor()






"""
import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='tmooc',db='tedu',charset='utf8')
cursor = conn.cursor()
sql1 = "insert into departments VALUES (%s,%s)"
result = cursor.execute(sql1,(4,'test')) #执行一个值
sql2 = "insert into departments VALUES (%s,%s)"
data = [(7,'sq'),(8,'te')]
data = [[9,'sq1'],[10,'te1']]
result = cursor.executemany(sql2,data) #执行多个值
print(result)
conn.commit()
cursor.close()
conn.close()
