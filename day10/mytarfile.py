#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import tarfile
tar = tarfile.open('/tmp/abc.tar.gz','w:gz') #创建压缩文件
tar.add('/etc/hosts') #添加文件
tar.close() #关闭

star = tarfile.open('/tmp/abc.tar.gz','r:gz')
star.extractall('/tmp/')  #解压缩
star.close()