#时间复杂度
#只是个估计
#时间复杂度相等，运行时间不一定相同

print('Hello world')  #O(1)

for i in range(n):
    print('Hello world')   # 共执行n次  #O(n)

for i in range(n):
    for j in range(n):
        print('Hello world')  #O(n**2)

for i in range(n):
    for j in range(n):
        for k in range(n):
            print('Hello world')  #共执行 n**3 次  #O(n**3)


print('Hello world')
print('Hello Python')
print('Hello Dandy')    #不是O(3) #O(1)


for i in range(n):
    print('Hello world')
    for j in range(n):
        print('Hello world')   #共执行 (n**2 + n) 次  #O(n**2)


for i in range(n):
    for j in range(i):
        print('Hello world')  #O(n**2)

while n > 1:
    print(n)
    n = n//2    #共执行 log2(n)次    #O(logn)   #每迭代一次，循环规模减半
#O(logn) << O(n)
#O(1) < O(logn) < O(n) < O(nlogn) < O(n**2) < O(logn * (n**2)) < O(n**3)
#看有几层循环

#空间复杂度
#内存可以买，时间不能  #空间换时间
