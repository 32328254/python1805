#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
compute = random.randint(1,10)


tag = 0

while tag == 0:
    people = int(input("please input you number:"))
    print("compute guess is",compute,"people guess is ",people)
    if compute == people:
        tag = 1
        print("ok")
    elif people > compute:
        print("guess big")
    else:
        print("guess small")
    a = input("Continue yes/no")
    if a == 'yes':
        continue
    else:
        break
