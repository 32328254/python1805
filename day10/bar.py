#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import foo
import foo as f
import demo.foo
from demo import foo
from demo import *

#print(foo.hi)
print(foo.fun())
print(f.fun())
####
print(demo.foo.fun())
print(foo.fun)
print(foo.hi)
