from functools import reduce


def AddSum(a,n):
    temp = 0
    ele = []
    sum = 0
    for i in range(1,n+1):
        temp = temp + a
        a = a * 10
        ele.append(temp)
    sum = reduce(lambda x,y:x+y, ele)
    return sum


if __name__ == '__main__':
    a = int(input("输入a的值："))
    n = int(input("输入n的值："))
    sum = AddSum(a, n)
    print('和为%d' %sum)