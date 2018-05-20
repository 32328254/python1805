#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import string
import sys
import subprocess

def get_password(length=8):
    result = ''
    for i in range(length):
        choice = random.choice(string.ascii_letters + string.digits)
        result += choice
    return result

def user_add(username,fname):
    data = """
user info:
username: %s
password: %s
    """
    passwords = get_password(8)
    subprocess.call('useradd %s'%(username),shell=True)
    subprocess.call('echo %s | passwd --stdin %s &> /dev/null'%(passwords,username),shell=True)
    with open(fname,'a') as f:
        f.write(data%(username,passwords))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s username fname"%sys.argv[0])
    user_add(sys.argv[1],sys.argv[2])
