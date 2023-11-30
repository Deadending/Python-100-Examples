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

# 009：暂停输出
## 题目：暂停1s输出
```python
import time

my_list = [1,2,3,4]
for i in my_list:
    print(time.strftime("%H:%M:%S",time.localtime()),":",i)
    time.sleep(1)
```

# 010：格式化输出时间
## 题目：暂停1s输出，并格式化当前时间
```python
import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
```

# 011：兔子数量
## 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
## 程序分析：将兔子分为1月兔、2月兔以及成年兔
```python
month = int(input("一共几个月："))
rabbit_1 = 1         # 一月兔数量
rabbit_2 = 0         # 二月兔数量
rabbit_elder = 0        # 成年兔数量
for i in range(month):
    print("第%d个月共有"%(i+1), rabbit_1 + rabbit_2 +rabbit_elder,"对兔子，其中")
    print("1月兔数量：", rabbit_1)
    print("2月兔数量：", rabbit_2)
    print("成年兔数量：", rabbit_elder) 
    rabbit_1, rabbit_2, rabbit_elder = rabbit_elder + rabbit_2, rabbit_1, rabbit_elder + rabbit_2
```

# 012：素数计算
## 题目：判断101-200之间有多少个素数，并输出所有素数。
## 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　
```python
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
```

# 013：水仙花数
## 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
## 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
- 实现方法一
```python
l = []
for n in range(100,1000):
    i = n // 100     #百位数
    j = n // 10 % 10 #十位数
    k = n % 10      #个位数
    if n == i**3 + j**3 + k**3:
        l.append(n)

print("所有的水仙花数为：", l)
```

- 实现方法二
```python
l = []
for n in range(100,1000):
    s = str(n)
    if n == int(s[0])**3 + int(s[1])**3 + int(s[2])**3:
        l.append(n)
print("所有的水仙花数为：", l)
```

# 14：因数分解
## 题目：将一个正整数分解质因数
## 程序分析：对n进行质因数分解，应先找到一个最小的质数k，然后按下述步骤完成：
1）if n==k，完成；
2）if n<>k，但n能被k整除，则打印k，并n=n/k，重复1）
3）如果n不能被k整除，则k=k+1，重复1）
```python
def ReduceNum(n):
    print('{} = '.format(n),end=" ")
    if not isinstance(n,int) or n<= 0:
        print("请输入一个正确的数字！")
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:
        for index in range(2,n+1):
            if n % index == 0:
                n = n // index
                if n == 1:
                    print(index)
                else:
                    print('{} *'.format(index),end=" ")
                break


if __name__ == "__main__":
    num = int(input("输入要被分解的数："))
    ReduceNum(num)
```

# 15：条件嵌套
## 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
## 程序分析：(a>b) ? a : b
- 实现方法一
```python
def ScoreLevel(score):
    if score>= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    else:
        return 'C'

if __name__ == "__main__":
    score = int(input("输入分数：\n"))
    level = ScoreLevel(score)
    print("%d 属于 %s" %(score, level))

```
- 实现方法二
```python
score = int(input("输入分数：\n"))
level = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
print("%d 属于 %s" %(score, level))
```

# 016:日期格式
## 题目：输出指定格式的日期
```python
import datetime
import time


if __name__ == "__main__":
    print(time.time())
    print(time.localtime())
    print(time.asctime())
    print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))
    print(time.strftime('%H-%M-%S %d-%m-%Y', time.localtime()))

    print(datetime.date.today().strftime('%d-%m-%Y'))
```

# 017：字符统计
## 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
```python
import string

def String_Count(s):
    letters = 0
    space = 0
    digit = 0
    others = 0
    for ele in s:
        if ele.isalpha():
            letters += 1
        elif ele.isspace():
            space += 1
        elif ele.isdigit():
            digit += 1
        else:
            others += 1
    return letters,space,digit,others


if __name__ == '__main__':
    s = input("输入一个字符串：")
    (letters,space,digit,others) = String_Count(s)
    print("字母%d个，空格%d个，数字%d个，其他%d个" %(letters,space,digit,others))
```

# 018：数列求和一
## 题目：求s=a+aa+aaa+aa...a的值，a和n由外部输入
```python
from functools import reduce


def AddSum(a,n):
    temp = 0
    ele = []
    sum = 0
    for i in range(1,n+1):
        temp = temp + a
        a = a * 10
        ele.append(temp)
    sum = reduce(lambda x,y:x+y, ele)
    return sum


if __name__ == '__main__':
    a = int(input("输入a的值："))
    n = int(input("输入n的值："))
    sum = AddSum(a, n)
    print('和为%d' %sum)
```

# 019:求“完数”
## 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
- 实现方法一
```python
import math
def ReduceNum(num):
    sum = 1
    for i in range(2,math.ceil(math.sqrt(num))):
        if num % i == 0:
            sum = sum + i + num / i
    return sum


if __name__ == '__main__':
    goal = []
    n = int(input("输入完数范围："))
    for i in range(3,n):
        sum = ReduceNum(i)
        if i == sum:
            goal.append(i)
    print('完数有：', goal)
```

- 实现方法二
```python
import math

n = int(input("输入完数范围："))
goal = []
for i in range(2,n+1):
    sum = 1
    ele = [1]
    for j in range(2,math.ceil(math.sqrt(i))):
        if i % j == 0:
            ele.append(j)
            ele.append(i/j)
            sum = sum + j + i/j
    if sum == i:
        goal.append(i)
        print('%d为完数' %i)
        ele.sort()
        print(ele)
print('完数有：', goal)
```

# 020：自由落体
## 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
```python
height = int(input("输入起始高度："))   #起始高度
times = int(input("输入落地次数："))    #下降次数

height_list = []     #每一次反弹后的高度

for i in range(1, times + 1):
    height = height/2
    height_list.append(height)

print('第%d次落地后共经过%f米' %(times,sum(height_list) * 2 + 100))
print('第%d次反弹%f米高' %(times,height_list[-1]))
```

# 021：猴子吃桃
## 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少？
```python
num = 1     #最后剩下一个
days = int(input('输入天数：'))
for i in range(0,9):
    num = (num + 1) * 2
print('第一天一共摘了%d个桃子' %num)
```

# 022：比赛名单
## 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
```python
for a in ['y', 'z']:
    for b in ['x', 'y', 'z']:
        for c in ['y']:
            if (a != b) and (b != c) and (c != a):
                print('比赛选手名单为:a--%s,b--%s,c--%s' %(a, b, c))
```

# 023：菱形打印
## 题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
```python
lines = int(input('输入菱形行数（奇数）：'))
mid = int(lines / 2) + 1        #中间行号
for i in range(1,lines + 1):
    space = abs(mid - i)        #空格数
    print(' ' * space, '*' * (2 * (mid - space)  -1))
```

# 024：数列求和二
## 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
```python
a = 2
b = 1
seq = []    #数列集合
n = int(input('输入项数：'))
for i in range(1, n + 1):
    seq.append(a / b)
    b, a = a, a + b
print('前%d项的和为%f' %(n, sum(seq)))
```

# 025：数列求和三
## 题目：求1+2!+3!+...+20!的和。
```python
n = int(input('输入项数：'))
a = 1
seq = []        #数列元素
for i in range(1, n + 1):
    a = a * i
    seq.append(a)
print('前%d项的和为%ld' %(n, sum(seq)))
```

# 026：递归求阶乘
## 题目：利用递归方法求5!。
```python
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

n = int(input('输入阶乘项数：'))
print(fac(n))
```

# 027：倒序打印
## 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
```python
def Reverse_Order(l,n):
    if n == 0:
        return
    print(l[n - 1])
    Reverse_Order(l,n-1)


l = input('输入一个字符串：')
n = len(l)
Reverse_Order(l,n)
```

# 028：岁数计算
## 题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
```python
def Age(n):
    if n == 1:
        return 10
    else:
        return Age(n - 1) + 2
    
print(Age(5))
```

# 029：数字分解
## 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
- 实现方法一
```python
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
```
- 实现方法二
```python
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
```

# 030：回文数
## 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
```python
x = int(input('输入一个整数：'))
x_str = str(x)
x_str_reverse = x_str[::-1]
if x_str == x_str_reverse:
    print(x,'是一个回文数！')
else:
    print(x,'不是一个回文数！')
```