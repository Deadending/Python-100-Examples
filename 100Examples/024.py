a = 2
b = 1
seq = []    #数列集合
n = int(input('输入项数：'))
for i in range(1, n + 1):
    seq.append(a / b)
    b, a = a, a + b
print('前%d项的和为%f' %(n, sum(seq)))