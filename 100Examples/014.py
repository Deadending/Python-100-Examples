def ReduceNum(n):
    print('{} = '.format(n),end=" ")
    if not isinstance(n,int) or n<= 0:
        print("请输入一个正确的数字！")
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:
        for index in range(2,n+1):
            if n % index == 0:
                n = n // index
                if n == 1:
                    print(index)
                else:
                    print('{} *'.format(index),end=" ")
                break


if __name__ == "__main__":
    num = int(input("输入要被分解的数："))
    ReduceNum(num)