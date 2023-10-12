import math

l = []
for i in range(100,200):
    flag = 1
    for j in range(2,round(math.sqrt(i))+1):
        if i%j == 0:
            flag = 0
            break
    if flag == 1:
        l.append(i)

print("101~200之间的素数一共有%d个" %len(l))
print(l)