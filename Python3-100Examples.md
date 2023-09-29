题目来自于Python菜鸟教程Python 100例，链接：https://www.runoob.com/python/python-100-examples.html
全部代码在Python 3.7 环境下运行。

# 001：数字组合
## 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
## 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。

- 实现方法一
```python
number = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j != k) and (k != i):
                number.append([i,j,k])
print("一共有%d个互不相同且无重复的三位数，分别是" %(len(number)))
print(number,end='\n')
```
- 实现方法二
```python
d = [(x,y,z) for x in range(1,5) for y in range(1,5) for z in range(1,5) if (x!=y) and (x!=z) and (y!=z)]
print("一共有%d个互不相同且无重复的三位数，分别是" %(len(d)))
print(d)
```
- 实现方法三
```python
from itertools import permutations
sum = 0
a = [1,2,3,4]
for i in permutations(a,3):
    print(i)
    sum += 1
print("一共有%d个互不相同且无重复的三位数" %sum)
```

# 002：个税计算
## 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
## 程序分析：利用数轴来分界，定位。
- 实现方法一
```python
profit = int(input("输入本月利润(万元)："))
profit_list = [100,60,40,20,10,0]
rate_list = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for i in range(len(profit_list)):
    if profit > profit_list[i]:
        bonus += (profit - profit_list[i])*rate_list[i]
        profit = profit_list[i]
print("奖金为%d" %(bonus*10000))
```

- 实现方法二
```python
profit = int(input("输入本月利润(万元)："))
profit_dict = {100:0.01, 60:0.015, 40:0.03, 20:0.05, 10:0.075, 0:0.1}
keys = profit_dict.keys()
bonus = 0
for key in keys:
    if profit > key:
        bonus += (profit - key)*profit_dict.get(key)
        profit = key
print("奖金为%d" %(bonus*10000))
```

# 003：平方数计算
## 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
## 程序分析：先求出所求数的最大范围，在循环求解
- 实现方法一
```python
# 求所求数范围：
n = 0
while ((i+1)**2 - i**2) <= 168:
    n += 1
for i in range(1,n):
    for j in range(i,n):
        if j*j - i*i == 168:
            print(j*j-268)
```

- 实现方法二：暴力求解
```python
print([n**2-100 for m in range(1,168) for n in range(1,m) if(m+n)*(m-n)==168])
```

# 004：日期计算
## 题目：输入某年某月某日，判断这一天是这一年的第几天？
## 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
- 实现方法一
```python
year = int(input("year:\n"))
month = int(input("month:\n"))
day = int(input("day:\n"))

#month = 31,28,31,30, 31, 30, 31, 31, 30, 31, 30,31
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print("Input Error!")
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and year % 100 != 0):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print("it is the %dth days." %sum)
```

- 实现方法二
```python
year = int(input("year:\n"))
month = int(input("month:\n"))
day = int(input("day:\n"))
sum = 0
months = (0,31,28,31,30, 31, 30, 31, 31, 30, 31, 30)
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    months[2] += 1
for i in range(month):
    sum += months[i]
print("it is the %dth day." % (sum + day))
```

# 005：三数比较
## 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
## 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

- 实现方法
```python
raw = []
for i in range(3):
    x = int(input("输入一个整数："))
    raw.append(x)
raw.sort()
print(raw)
```

# 006 斐波那契数列
```python
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
```

# 007：列表复制
## 题目：将一个列表的数据复制到另外一个列表
## 程序分析：使用列表[:]
```python
n = int(input("输入列表中元素个数："))
a_list = []
b_list = []
for i in range(1, n + 1):
    print("第%d个元素为：" %i,end="")
    temp = int(input())
    a_list.append(temp)
b_list = a_list[:]
print("a_list:",a_list,"b_list:",b_list)
```

# 008:99乘法表
## 题目：输出9*9乘法口诀表
## 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
```python
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print("%2d *%2d = %2d" %(j, i, j*i),end=" ")
```