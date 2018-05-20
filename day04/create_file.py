#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os


def get_filename():
    while True:
        file_name = input('please input you file name: ')
        if not os.path.exists(file_name):
            #return file_name #错误,return 值后while循环退出.
            get_info(file_name)
            break
        else:
            print(file_name, "exits,please try input age!!!")
    #return file_name

def get_info(filename):
    info_list = []
    while True:
        data = input("please input you information[input q is quit]: ")
        if not data == "q":
            info_list.append(data)
        else:
            print("thanks you used")
            print(info_list)
            with open(filename,'w+') as f:
                for i in info_list:
                    i = i + '\n'
                    f.write(i)
                #f.writelines(info_list)
            break


if __name__ == '__main__':
    #a = get_filename()
    #print(a)
    get_filename()
    #get_info('liu.txt')
