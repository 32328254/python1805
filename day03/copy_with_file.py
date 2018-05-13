#!/usr/bin/env python3
# -*- coding:utf-8 -*-
source_fname = '/bin/ls'
dst_fname = '/tmp/list'

with open(source_fname,'rb') as src_fobj:
    with open(dst_fname,'wb') as dst_fobj:
        while True:
            data = src_fobj.read(4096)
            if not data:
                break
            else:
                dst_fobj.write(data)