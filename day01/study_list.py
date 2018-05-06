#!/usr/bin/env python3
# -*- coding:utf-8 -*-
alist = [1,5,10,'bob','alice',[1,2,3]]
alist[-3:-1] #列表切片
print(alist[-3:-2])
alist[-1] = 100 #修改列表某个值
10 in alist #关系成员判断
alist.append(50) #追加
alist.insert(1,200) #插入
print(alist)
##################################################
atuple = (10,20,30,'bob','alice') #不可修改的list
atuple[:3] #取值
blist = alist[:] #在内存中不指向同一块内存空间,这样的话修改alist时blist步会改变
