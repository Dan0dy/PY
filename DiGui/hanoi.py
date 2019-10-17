#汉诺塔
#n = 2 ，3部
#n个时， 把n-1个移动到B，把第n个移动到c， 再把n-1个移动到C

def h(n, A, B, C):
    if n > 0:
        h(n-1, A, C, B)  #把前n-1个从A通过C移到B
        print('%s -> %s' %(A, C))  #把第n个从A移动到c
        h(n-1,B, A, C)   #再把前n-1个从B通过A移到C
#h(n) = 2h(n-1) +1

def h1(n):
    if n == 1:
        return 1
    elif n > 1:
        return 2*h1(n-1) + 1
h(3, 'A', 'B','C')
print(h1(3))

