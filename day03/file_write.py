#!/usr/bin/env python3
# -*- coding:utf-8 -*-
f = open('abc.txt','w') #文件存在则清空，文件不存在则创建
f.write('hello world\n')
f.writelines(['how are you?\n','nice to meet you\n','me to\n']) #写一个列表到文件中
f.writable()  #是否可写
f.flush()     #立即将数据同步到硬盘,否则将写缓存区,默认4096KB同步一次
f.close()