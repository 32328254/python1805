#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
compute = random.randint(1,10)

tries = 0

while tries < 3:
    people = int(input("please input you number,yes/no:"))
    if people == 0:
        break
    print("compute guess is",compute,"people guess is ",people)
    if compute == people:
        print("ok")
    elif people > compute:
        print("guess big")
    else:
        print("guess small")
    tries += 1
else:
    print("the number is:",compute)