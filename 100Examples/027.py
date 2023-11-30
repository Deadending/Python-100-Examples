def Reverse_Order(l,n):
    if n == 0:
        return
    print(l[n - 1])
    Reverse_Order(l,n-1)


l = input('输入一个字符串：')
n = len(l)
Reverse_Order(l,n)