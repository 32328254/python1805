#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
alist = [1,2,20,10,45,40,24]
alist.append(3) #追加
alist.insert(0,0) #在下标为0的地方插入0
alist.count(1) #统计1出现的次数
alist.extend('new') #把new内容中每一项添加在列表中
alist.index(1) #获得下标
alist.reverse() #取反
alist.sort() #排序,但类型必须一样，否则报错
alist.pop() #弹出列表中的最后一项
alist.pop(1) #弹出下标为1的项
alist.remove('new') #移除列表中的项
blist = alist.copy() #将alist的值赋值给blist
blist.clear() #清空列表

#打乱列表
random.shuffle(alist)
print(alist)
