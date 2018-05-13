#!/usr/bin/env python3
# -*- coding:utf-8 -*-
source_file = '/bin/ls'
dest_file = '/root/test/'
file_name = 'ls'

s_file = open(source_file,'rb')
d_file = open(dest_file+file_name,'wb')
for line in s_file:
    d_file.write(line)
s_file.close()
d_file.flush()
d_file.close()