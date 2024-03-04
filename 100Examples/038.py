if __name__ == '__main__':
    n = int(input("请输入矩阵大小："))
    a = []
    sum = 0.0
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(float(input("输入矩阵元素：\n")))
    
    for i in range(n):
        sum += a[i][i]
    
    print(a)
    print(sum)