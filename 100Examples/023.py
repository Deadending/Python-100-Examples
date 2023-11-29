lines = int(input('输入菱形行数（奇数）：'))
mid = int(lines / 2) + 1        #中间行号
for i in range(1,lines + 1):
    space = abs(mid - i)        #空格数
    print(' ' * space, '*' * (2 * (mid - space)  -1))