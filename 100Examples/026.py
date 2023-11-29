def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

n = int(input('输入阶乘项数：'))
print(fac(n))