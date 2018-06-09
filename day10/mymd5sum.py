#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib
import sys
def check_md5(file):
    m = hashlib.md5()
    with open(file,'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
    #m = hashlib.md5()
    #m = hashlib.md5()
            m.update(data)
    #print(m.hexdigest())
    return m.hexdigest() #获取值
if __name__ == '__main__':
    try:
        fn = sys.argv[1]
    except IndexError as e:
        print("%s follow a file as argument" %__file__)  #__file__ 获取脚本名
        sys.exit(1)
    value = check_md5(fn)
    print("%s md5sum value is %s"%(fn,value))