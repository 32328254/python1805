#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def blocks(fobj):
    lines = []
    count = 0
    for line in fobj:
        lines.append(line)
        count += 1
        if count == 10:
            yield lines
            lines = []
            count = 0
    if lines:
        yield lines

if __name__ == '__main__':
    fobj = open('/etc/password')
    for data in blocks(fobj):
        print(data)
    fobj.close()