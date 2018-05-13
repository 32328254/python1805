#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#source_fname = '/bin/ls'
#dst_fname = '/tmp/list'
def copy_func(sour_fname,dst_fname):
    with open(source_fname,'rb') as src_fobj:
        with open(dst_fname,'wb') as dst_fobj:
            while True:
                data = src_fobj.read(4096)
                if not data:
                    break
                else:
                    dst_fobj.write(data)
            return "ok"
if __name__ == '__main__':
    source_fname = input('please input source file name:')
    dst_fname = input('please input destination file name:')
    status =  copy_func(source_fname,dst_fname)
    print(status)