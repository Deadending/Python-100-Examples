# import math
# def ReduceNum(num):
#     sum = 1
#     for i in range(2,math.ceil(math.sqrt(num))):
#         if num % i == 0:
#             sum = sum + i + num / i
#     return sum


# if __name__ == '__main__':
#     goal = []
#     n = int(input("输入完数范围："))
#     for i in range(3,n):
#         sum = ReduceNum(i)
#         if i == sum:
#             goal.append(i)
#     print('完数有：', goal)

import math

n = int(input("输入完数范围："))
goal = []
for i in range(2,n+1):
    sum = 1
    ele = [1]
    for j in range(2,math.ceil(math.sqrt(i))):
        if i % j == 0:
            ele.append(j)
            ele.append(i/j)
            sum = sum + j + i/j
    if sum == i:
        goal.append(i)
        print('%d为完数' %i)
        ele.sort()
        print(ele)
print('完数有：', goal)