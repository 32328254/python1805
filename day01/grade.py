#!/usr/bin/env python3
# -*- coding:utf-8 -*-
try:
    grade = int(input('plase input you grade:'))
    print(grade)
    if grade >= 90:
        print('very good')
    elif 90 > grade >= 80:
        print('good')
    elif 80 > grade >= 70:
        print('fine')
    elif 70 > grade >= 60:
        print('pass')
    else:
        print('fuck you!!!')
except Exception as e:
    print("ERROR:",e)

