if __name__ == '__main__':
    sum = 4
    i = 4
    for j in range(2,9):
        if j <= 2:
            i = i * 7
        else:
            i = i * 8
        sum += i
        print("0—7能组成%7d个%d位数奇数" %(i, j))
    print("0—7一共能组成%d个奇数" %sum)