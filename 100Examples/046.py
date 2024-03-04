TRUE = 1
FALSE = 0
def Square(x):
    return x * x
flag = 1
while flag:
    num = int(input('请输入一个数字：'))
    print('运算结果为：%d' % (Square(num)))
    if Square(num) >= 50:
        flag = TRUE
    else:
        flag = FALSE