#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib
m = hashlib.md5()
m.update('abc'.encode('utf-8'))
print(m.hexdigest())
