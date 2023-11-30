n = int(input('输入一个整数：'))
a = n // 10000
b = n % 10000 // 1000
c = n % 1000 // 100
d = n % 100 //10
e = n % 10
if a != 0:
    print('5位数：',e,d,c,b,a)
elif b != 0:
    print('4位数：',e,d,c,b)
elif c != 0:
    print('3位数：',e,d,c)
elif d != 0:
    print('2位数：',e,d)
else:
    print('1位数：',e)


n = int(input('输入一个整数：'))
n_str = str(n)
n_str_reverse = n_str[::-1]
n_len = len(n_str)
if n_len == 5:
    print('5位数：',n_str_reverse)
elif n_len == 4:
    print('4位数：',n_str_reverse)
elif n_len == 3:
    print('3位数：',n_str_reverse)
elif n_len == 2:
    print('2位数：',n_str_reverse)
elif n_len == 1:
    print('1位数：',n_str_reverse)
