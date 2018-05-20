#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
列表解析
"""
[10]
[10 + 5]
[10 +5 for i in range(5)]
[10 + i for i in range(1,6)]
[10 +i for i in range(1.11) if i %2]
[10 + i for i in range(1,11) if i %2 == 1]
content = ['hello','world']
content = ['%s\n'%line for line in content]