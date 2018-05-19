#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import shutil
import os

# src = open('/etc/hosts','rb')
# dst = open('/tmp/hostname','wb')
# shutil.copyfileobj(src,dst) #copy文件对象
# src.close()
# dst.close()

with open('/etc/hosts', 'rb') as src:
    with open('/tmp/hostname', 'wb') as dst:
        shutil.copyfileobj(src, dst)  # copy文件对象

shutil.copyfile('/etc/hosts', '/tmp/hostname')  # 通过文件名copy,之copy文件内容,
shutil.copymode('/etc/hosts', '/tmp/hostname')  # copy 权限
shutil.copystat('/etc/hosts', '/tmp/hostname')  # copy元数据
shutil.copy('/etc/hosts', '/tmp/')  # 将文件名hostscopy至/tmp目录下
shutil.copy2('/etc/hosts', '/tmp/')  # 相当于linux 中的 cp -p
shutil.copytree()  # copy目录,
shutil.rmtree('/tmp')  # 删除目录
shutil.move('/tmp/hostname', '/tmp/hosts')  # 移动,包括文件或目录
shutil.chown('/tmp/hostname', 'user=admin', 'group=admin')  # 修改文件拥有者
os.remove('/tpm/hostname')  # 删除文件
