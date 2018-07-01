#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import subprocess
import os
def ping_ip(host):
    #status = subprocess.call('ping -c2 %s &>/dev/null' %host,shell=True)
    status = subprocess.call('ping -c2 %s' % host, shell=True)
    print(status)
    if status == 0:
        print("%s: up"%host)
    else:
        print("%s:down"%host)

if __name__ == '__main__':
    ips = ['172.40.51.%s'%i for i in range(1,255)] #列表解析
    for ip in ips:
        fock_status = os.fork()
        if fock_status == 0:
            ping_ip(ip)
            exit() #子进程退出

