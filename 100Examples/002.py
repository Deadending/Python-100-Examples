'''
@Func: 个税计算
@Author：jlzhong0709@gmail.com
@Date:12/05/2023
'''

profit = int(input("输入本月利润(万元)："))
profit_list = [100,60,40,20,10,0]
rate_list = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for i in range(len(profit_list)):
    if profit > profit_list[i]:
        bonus += (profit - profit_list[i])*rate_list[i]
        profit = profit_list[i]
print("奖金为%d" %(bonus*10000))


profit = int(input("输入本月利润(万元)："))
profit_dict = {100:0.01, 60:0.015, 40:0.03, 20:0.05, 10:0.075, 0:0.1}
keys = profit_dict.keys()
bonus = 0
for key in keys:
    if profit > key:
        bonus += (profit - key)*profit_dict.get(key)
        profit = key
print("奖金为%d" %(bonus*10000))