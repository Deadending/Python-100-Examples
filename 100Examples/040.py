if __name__ == '__main__':
    list_before = [9,6,5,4,1]
    print('原始列表为：', list_before)
    l = len(list_before)
    # 方法一：位置交换
    for x in range(l //2 ):
        list_before[x],list_before[l - x - 1] = list_before[l - x - 1],list_before[x]
    list_after = list_before[:]
    print('原始列表为：', list_after)

    # 方法二：reverse函数
    list_before.reverse()
    list_after = list_before[:]
    print('原始列表为：', list_after)