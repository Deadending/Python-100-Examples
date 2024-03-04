if __name__ == '__main__':
    x = int(input('请输入一个数字：'))
    y = int(input('请输入另外一个数字：'))
    if x > y:
        print('%d 大于 %d' %(x,y))
    elif x == y:
        print('%d 等于 %d' %(x,y))
    else:
        print('%d 小于 %d' %(x,y))