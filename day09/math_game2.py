#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
lambda匿名函数
"""

import random

"""
def add(x, y):
    return x + y


def sub(x, y):
    return x - y
"""

def exam():
    tries = 0
    cmds = {'+': lambda x,y:x + y, "-": lambda x,y: x - y}  #lamdba匿名函数,取代了add和sub两个函数
    nums = [random.randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 这注意
    print(nums)
    op = random.choice('+-')
    result = cmds[op](*nums)
    prompt = "%s %s %s = " % (nums[0], op, nums[1])
    while tries < 3:
        try:
            answer = int(input(prompt))
        except:
            continue
        if answer == result:
            print("right")
            break
        print("Wrong answer.Try again.")
        tries += 1
    else:
        print("right result is %s %s" % (prompt, result))


def main():
    while True:
        exam()
        try:
            yn = input("Continue(y/n)?").strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print("bye bye")
            yn = 'N'
        if yn in 'nN':
            break


if __name__ == '__main__':
    main()
