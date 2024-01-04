import math 
prime_list = []

N = int(input("输入一个整数："))
for num in range(2,N + 1):
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            break;
    else:
        prime_list.append(num)

print("%d以内的素数个数为：%d，分别为" %(N, len(prime_list)))
print(prime_list)