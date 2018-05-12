#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
prompt = """\033[31;1m
[0]剪刀:shears
[1]石头:stone
[3]布:cloth
you choice[0/1/2]:
\033[0m"""

win_list = [['shears','cloth'],['cloth','stone'],['stone','shears']]

all_choice = ['shears','cloth','stone']

compute = random.choice(all_choice)

#print(compute)
ind = int(input(prompt))
people = all_choice[ind]
#print(people)
print("compute choice is",compute," people choice is",people)

if people == compute:
    print("\033[32;1mgodfall\033[0m")
elif [people,compute] in win_list:
    print("\033[31;1mpeople win\033[0m")
else:
    print("\033[31;1mpeople lost\033[0m")