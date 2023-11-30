x = int(input('输入一个整数：'))
x_str = str(x)
x_str_reverse = x_str[::-1]
if x_str == x_str_reverse:
    print(x,'是一个回文数！')
else:
    print(x,'不是一个回文数！')