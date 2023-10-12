l = []
for n in range(100,1000):
    i = n // 100     #百位数
    j = n // 10 % 10 #十位数
    k = n % 10      #个位数
    if n == i**3 + j**3 + k**3:
        l.append(n)

print("所有的水仙花数为：", l)

l = []
for n in range(100,1000):
    s = str(n)
    if n == int(s[0])**3 + int(s[1])**3 + int(s[2])**3:
        l.append(n)
print("所有的水仙花数为：", l)
