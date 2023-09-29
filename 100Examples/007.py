n = int(input("输入列表中元素个数："))
a_list = []
b_list = []
for i in range(1, n + 1):
    print("第%d个元素为：" %i,end="")
    temp = int(input())
    a_list.append(temp)
b_list = a_list[:]
print("a_list:",a_list,"b_list:",b_list)