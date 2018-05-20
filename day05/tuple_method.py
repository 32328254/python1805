#!/usr/bin/env python3
# -*- coding:utf-8 -*-
atuple = (10,29)
atuple.count(10) #统计10出现的次数
atuple.index(1) # 下标为1的项
#如果元组是单个需要加逗号
btuple = (200,)

#如果元组里包含可变对象,那么可变对象是可变的
a = (10,[1,2,3])
a[1].append(10)