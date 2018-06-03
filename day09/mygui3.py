#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import tkinter
from functools import partial


def say_hi(world):
    def welcome():
        label.config(text='Hello %s' % world)

    return welcome


root = tkinter.Tk()
label = tkinter.Label(text='Hello world', font="15px")
b1 = tkinter.Button(root, bg='red', fg='white', text='button1', comand=say_hi('sss'))
MyButton = partial(tkinter.Button(root, bg='red', fg='white'))  # 偏函数
b2 = MyButton(text='button2', command=say_hi('chine'))
b3 = MyButton(text='quit', command=root.quit())
label.pack()  # ?
b1.pack()
b2.pack()
b3.pack()
root.mainloop()  # ?
