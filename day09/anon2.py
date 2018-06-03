"""
filter() 高阶函数，返回真假,0,1
"""
from random import randint

def func1(x):
    return x % 2 #返回0或1


if __name__ == '__main__':
    nums = [randint(1,100) for i in range(10)]
    for i in filter(func1,nums):
        print(i)
    ##########################################
    for i in filter(lambda x:x%2,nums):
        print(i)

