#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import tarfile
import hashlib
import os
import mymd5sum
import pickle

md5file = '/tmp/md5file.dat'
local_time = time.strftime('%Y-%m-%d-%H-%M-%S')


def getDfile(src_dir, dest_dir, tag):
    sfile = os.path.basename(src_dir.rstrip("/"))  # 获取原文件名
    dest_dir = dest_dir.rstrip("/")  # 获取目标目录
    bfile = "%s-%s-%s.tar.gz" % (sfile, tag, local_time)  # 备份文件名
    dst_file = os.path.join(dest_dir, bfile)  # 拼接路径
    return dst_file


def full_back(src_dir, dest_dir):
    dst_file = getDfile(src_dir, dest_dir, tag='full')
    file = tarfile.open(dst_file, 'w:gz')
    file.add(src_dir)
    file.close()

    md5dict = {}
    for path, dir, file in os.walk(src_dir):  # os.walk(path_dir) path_dir是个路径
        for i in file:
            fn = os.path.join(path, i)
            print(fn)
            md5dict[fn] = mymd5sum.check_md5(fn)
    print(md5dict)

    with open(md5file, 'wb') as fd:
        pickle.dump(md5dict, fd)


def incrback(src_dir, dest_dir):
    dst_file = getDfile(src_dir, dest_dir, tag='incr')

    md5dict = {}
    for path, dir, file in os.walk(src_dir):  # os.walk(path_dir) path_dir是个路径
        for i in file:
            fn = os.path.join(path, i)
            # print(fn)
            md5dict[fn] = mymd5sum.check_md5(fn)
    with open(md5file, 'rb') as fd:
        old_md5dict = pickle.load(fd)
    tar = tarfile.open(dst_file, 'w:gz')
    for k in md5dict:
        if old_md5dict.get(k) != md5dict[k]:
            tar.add(k)
    tar.close()

    with open(md5file, 'wb') as fd:
        pickle.dump(md5dict, fd)


if __name__ == '__main__':
    # print(time.strftime('%a'))
    if time.strftime('%a') == 'SuN':
        full_back('/home/liu/day10', '/tmp')
    else:
        incrback('/home/liu/day10', '/tmp')
