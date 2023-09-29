def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

num = int(input("斐波那契数列个数："))
fib_list = []
for i in range(1,num + 1):
    fib_list.append(fib(i))
    print(fib(i))
print(fib_list)