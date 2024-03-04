if __name__ == '__main__':
    list_before = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
    num = int(input("输入插入的数字："))
    list_before.append(num)
    list_after = list_before[:]
    for x in range(len(list_after), 0, -1):
        if num > list_after[x - 2]:
            list_after[x - 1] = num
            break
        else:
            list_after[x - 1]= list_after[x - 2]
    print("原始列表为：", list_before)
    print("排序后列表为：", list_after)