height = int(input("输入起始高度："))   #起始高度
times = int(input("输入落地次数："))    #下降次数

height_list = []     #每一次反弹后的高度

for i in range(1, times + 1):
    height = height/2
    height_list.append(height)

print('第%d次落地后共经过%f米' %(times,sum(height_list) * 2 + 100))
print('第%d次反弹%f米高' %(times,height_list[-1]))
    