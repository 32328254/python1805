#!/usr/bin/env python3
# -*- coding:utf-8 -*-
adict = {'name':'bob','age':'25'}
print(adict)
len(adict)
bdict = dict()
print(type(bdict))
cdict = dict([('name','bob'),('age',25)]) #列表中两个字符串,每个串中第一个ie为key,第二个为value
print(cdict)
ddict = {}.fromkeys(['zang','zhao','li'],23) #formkeys第一个
print(ddict)
'bob'  not in adict #false
'name' in adict #字典是通过key查找数据
adict['name'] ='tom'
adict['phone'] = '121231234' #更新
len(adict) #长度
hash() #判断是否可以当作字典key，key是不可变
adict.clear() #清空
adict.copy() #深copy
adict.keys() #返回所以key
adict.values() #返回所有的value
adict.items() #返回键值队
adict.pop('key')  #弹出给定的key
adict.popitem()  #随机弹出一项
adict.get('key')    #取不存在值时时Null，不会报错

adict.get('key','not found')  #没查到时返回not found
adict.setdefault('name','jerry')  #key不存在时赋值
