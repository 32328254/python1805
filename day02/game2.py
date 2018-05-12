#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
"""
剪刀:shears
石头:stone
布:cloth
"""

win_list = [['shears','cloth'],['cloth','stone'],['stone','shears']]

all_choice = ['shears','cloth','stone']

compute = random.choice(all_choice)
#print(compute)
people = input("you choice is [shears/cloth/stone]:")
#print(people)
print("compute choice is",compute," people choice is",people)

if people == compute:
    print("godfall")
elif [people,compute] in win_list:
    print("people win")
else:
    print("people lost")