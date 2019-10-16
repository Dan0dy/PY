#递归
#调用自身
#结束条件
from timewrap import *
def func1(x):
    if x > 0:
        print(x)
        func1(x-1)

def func2(x):   #先递归后打印
    if x > 0:
        func2(x-1)
        print(x)

func1(3)
func2(3)

#斐波那契数列 1 1 2 3 5 8
#F(n) = F(n-1) + F(n-2)
#F(0) =1, F(1)= 1

def fib1(n):       #O(2^n)
    if n == 0 or n == 1:
        return 1
    else:
        return fib1(n-1) + fib2(n-2)
@cal_time
def F1(n):
    return fib1(n)
#print(F1(34))
#print(func1.__name__)

#方法二 数组
@cal_time
def fib2(n):     #时间O(n)   #空间O(n)
    li = [1, 1]
    for i in range(2, n+1):
        li.append(li[-1] + li[-2])
    return li[n];
fib2(1000)

@cal_time
def fib3(n):
    a = 1
    b = 1
    c = 0
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1):
            c = a + b    # 1 2 3  #a b c
            a = b
            b = c        # 2 3 5  # a b c
        return c
fib3(1000)
