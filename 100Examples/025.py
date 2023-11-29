n = int(input('输入项数：'))
a = 1
seq = []        #数列元素
for i in range(1, n + 1):
    a = a * i
    seq.append(a)
print('前%d项的和为%ld' %(n, sum(seq)))