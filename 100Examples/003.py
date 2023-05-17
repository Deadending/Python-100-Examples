'''
@Func: 平方数计算
@Author：jlzhong0709@gmail.com
@Date:17/05/2023
'''

n = 0
while ((n+1)**2 - n**2) <= 168:
    n += 1
for i in range(1,n):
    for j in range(i,n):
        if j*j - i*i == 168:
            print(j*j-268)

print([n**2-100 for m in range(1,168) for n in range(1,m) if(m+n)*(m-n)==168])