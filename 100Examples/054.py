if __name__ == '__main__':
    x = int(input('Input a number:'))
    y = x >> 4
    c = ~(~0 << 4)
    x_output = y & c
    # 转换成二进制数
    x = bin(x)
    x_output = bin(x_output)
    print('%s \t %s' %(x, x_output))