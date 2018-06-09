#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import tarfile
import hashlib
import os
import sys
md5file = '/tmp/md5file.dat'
local_time = time.strftime('%Y-%m-%d')

def full_back(src_dir,dest_dir):
    sfile = os.path.basename(src_dir.rstrip("/")) #获取原文件名
    #print(sfile)
    dest_dir = dest_dir.rstrip("/")#获取目标目录
    print(dest_dir)
    bfile = "%s-%s.tar.gz"%(sfile,local_time)     #备份文件名
    print(bfile)
    dst_file = os.path.join(dest_dir,bfile)       #拼接路径
    print(dst_file)
    file = tarfile.open(dst_file,'w:gz')
    file.add(src_dir)
    file.close()

def incrback():
    pass

if __name__ == '__main__':
    if time.strftime('%a') == 'Sat':
        full_back('/etc/passwd','/tmp')
    else:
        incrback()