#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
thread对象使用start()方法开始线程执行,使用join()方法挂起程序,直到线程结束
"""

import threading
import subprocess

def my_ping(host):
    retval = subprocess.call('ping -c2 %s &>/dev/null '%host,shell=True)
    if retval == 0:
        print("%s up"%host)
    else:
        print("%s down"%host)

if __name__ == '__main__':
    ip_list = ['172.40.51.%s'%i for i in range(1,255)]
    for i in ip_list:
        t = threading.Thread(target=my_ping,args=(i,)) #创建多线程
        t.start()
        #t.join()