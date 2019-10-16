#n阶台阶，每次能上一节台阶或2个 共几种

def F(n):      #共有F(n)种走法
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return F(n-1) + F(n-2)   #第一次上一个 后面共F(n-1), 第一次上2个，后面共F(n-2)


print(F(2))
