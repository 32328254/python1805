#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
ER模型：
 ER是实体，关系的首字母
 ER模型的基本元素是：实体，联系和属性
 实体：是一个数据对象，指应用中可以区别的客观存在的事物,在ER关系模型中实体用方框表示
 属性：实体的某一特性称为属性，在ER关系模型中属性用椭圆形表示
 联系：表示一个或多个实体之间的关联关系,在ER关系模型中联系用菱形表示
"""
"""
数据库范式：
6个范式，一般到第三范式.
(1NF)第一范式：原子性(不可再分),数据库中的每一列都是不可分割的原子数据项.
(2NF)第二范式：实体的属性完全依赖于主关键字,所谓完全依赖式是指不能存在仅依赖主关键字一部分的属性，第二范式要求数据库表中每一条数据可以被唯一区分。
(3NF)第三范式：任何非主属性不能依赖其他非主属性.
"""
"""
数据库约束：
  主键约束：每一张表有一个主键字段.不能为空,必须唯一,且IMAGE和TEXT类型的列不能被指定为主关键字.
  外键约束：表之间的联系,外键列必须是其他表的主键.
  唯一性约束：数据在所有记录中必须唯一.
  检查约束：对表中列设定符合检查性.
  非空约束：字段必须有值，不能为空.
"""
"""
MariaDB [mysql]> show databases; #查看数据库
MariaDB [mysql]> CREATE DATABASE tarena DEFAULT CHARSET utf8; #创建数据库
MariaDB [mysql]> USE tarena; #进入数据库.
MariaDB [tarena]> SHOW TABLES; #查看有那些表.
MariaDB [tarena]> SELECT DATABASE(); #查看当前在哪个库.
MariaDB [tarena]> CREATE TABLE departments(dep_id INT,dep_name VARCHAR(20),PRIMARY KEY(dep_id));
MariaDB [tarena]> SHOW CREATE TABLE departments; #查看创建表语句.
MariaDB [tarena]> DESC departments; #查看表结构.
MariaDB [tarena]> alter table departments add constraint departments primary key(dep_id); #给表加主键
MariaDB [tarena]> DROP TABLE departments; #删除表
MariaDB [tarena]> create table departments(dep_id int(12),dep_name varchar(20) not null unique,primary key(dep_id));
MariaDB [tarena]> create table employees(emp_id int, emp_name varchar(20) not null unique,gender enum('male','female'),phone varchar(20),email varchar(50), dep_id int, primary key(emp_id),foreign key(dep_id) references departments(dep_id));
MariaDB [tarena]> create table salary(auto_id int auto_increment,date DATE,emp_id int,basic int,awards int,primary key(auto_id),foreign key(emp_id) references employees(emp_id));
MariaDB [tarena]> insert into departments values(1,'人事部');
MariaDB [tarena]> insert into employees values(1,'zs','male','12345678901','zs@qq.com,',1);
MariaDB [tarena]> insert into salary(date,emp_id,basic,awards) values('2018-07-07',1,1000,1000);
"""