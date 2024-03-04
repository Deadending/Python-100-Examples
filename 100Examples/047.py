def Exchange(a,b):
    a, b = b, a
    return (a, b)

if __name__ == '__main__':
    x = int(input('请输入一个数字：'))
    y = int(input('请输入另外一个数字：'))
    print('交换前x = %d, y = %d' %(x,y))
    x, y = Exchange(x,y)
    print('交换后x = %d, y = %d' %(x,y))