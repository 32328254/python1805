#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
pypi: python package index
http://pypi.python.org  可以在官方下载相应的python软件包
如果连接互联网，可以使用pip命令安装

pip连接的是pypi.python.org，在国外，速度慢，可以通过以下方式使用国内站点
1、创建配置文件目录
[root@room8pc16 weekend2018]# mkdir /root/.pip/
2、创建配置文件
[root@room8pc16 weekend2018]# gedit /root/.pip/pip.conf
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com

安装paramiko：python的ssh库
[root@room8pc16 weekend2018]# pip3 install paramiko
"""

import paramiko
import sys
import os
import getpass
import threading
def remote_comm(host,user,pwd,comm):
    ssh = paramiko.SSHClient()
    #下行相当于是ssh时问(yes/no),回答yes
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname=host, username=user, password=pwd)
    # 如果上面代码执行有异常发生，那么使用下面这个
    ssh.connect(hostname=host,username=user,password=pwd,allow_agent=False)
    stdin,stdout,stderr = ssh.exec_command(comm)
    out = stdout.read().decode('utf8')
    error = stderr.read().decode('utf8')
    if out:
        print('OUT %s:\n%s'%(host,out),end='')
    if error:
        print('ERROR %s:\n%s'%(host,error),end='')
    ssh.close()
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: %s ipfile username 'command'"%sys.argv[0])
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print("no such file:",sys.argv[1])
        sys.exit(2)
        ipfile = sys.argv[1]
        user = sys.argv[2]
        comm = sys.argv[3]
        pwd = getpass.getpass("password:")
        with open(ipfile) as fobj:
            for line in fobj:
                ip = line.strip()
                #remote_comm(ip,user,pwd,comm)
                #多线程
                t = threading.Thread(target=remote_comm,args=(ip,user,pwd,comm))
                t.start()