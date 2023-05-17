'''
@Func: 数字组合
@Author：jlzhong0709@gmail.com
@Date:12/05/2023
'''

# 1.循环遍历
number = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j != k) and (k != i):
                number.append([i,j,k])
print("一共有%d个互不相同且无重复的三位数，分别是" %(len(number)))
print(number,end='\n')

# 2.简便循环
d = [(x,y,z) for x in range(1,5) for y in range(1,5) for z in range(1,5) if (x!=y) and (x!=z) and (y!=z)]
print(d)

# 3.统计方法
from itertools import permutations
sum = 0
a = [1,2,3,4]
for i in permutations(a,3):
    print(i)
    sum += 1
print("一共有%d个互不相同且无重复的三位数" %sum)
