if __name__ == '__main__':
    a = 809
    for i in range(10,100):
        b = a * i
        if (b < 10000) and (8 * i < 1000) and (9 * i >= 100):
            print('??代表的是%d，809*??的结果是%d。' %(i, (809 * i)))