#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
print("1:剪刀,2:石头,3:布")
all_choice = [1,2,3]
compute = random.choice(all_choice)

people = int(input("please you choice: ['1:剪刀'/'2:石头'/'3:布']"))
print("compute is :",compute,"people is ",people)
if compute == people:
    print("godfall")
elif people == 1 and compute == 3:
    print("people win")
elif people == 2 and compute == 1:
    print("people win")
elif people == 3 and compute == 2:
    print("people win")
else:
    print("you lost")
