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