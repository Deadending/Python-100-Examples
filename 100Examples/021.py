num = 1     #最后剩下一个
days = int(input('输入天数：'))
for i in range(0,9):
    num = (num + 1) * 2
print('第一天一共摘了%d个桃子' %num)