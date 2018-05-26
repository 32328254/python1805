#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys


def unix2dos(file_name):
    new_file = 'new' + file_name
    with open(file_name,'r') as source_f:
        with open(new_file,'w') as new_f:
            for line in source_f:
                new_f.write(line.rstrip('\r\n')+'\r\n')

def dos2unix(file_name):
    data = ""
    with open(file_name,'r') as source_f:
        for line in source_f:
            data += line.rstrip('\r\n') + '\n'
    with open(file_name,'w') as new_f:
        new_f.write(data)


if __name__ == '__main__':
    file_name = sys.argv[1]
    #unix2dos(file_name)
    dos2unix(file_name)