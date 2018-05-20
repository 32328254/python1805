#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"{} is {} years olds".format('zhangsan','25') #顺序填充
"{0} is {1} years olds".format('zhangsan','25') #位置填充
adict = {"name":"zhangsan","age":25}
"{0[name]} is {0[age]} year old".format(adict) #字典方式
alist = ['zhangsan',25]
"{0[0]} is {0[1]} years old".format(alist) #列表方式

"{:>20}".format('name') #右对齐,20个宽度
"{:<20}".format('name') #左对齐.20个宽度
"{:^20}".format('name') #剧中,20宽度
"{:#>20}".format('name') #右对齐,20宽度,左侧用#填充


