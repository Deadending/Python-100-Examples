def Yanghui_Triangle(i,j):
    if i == 1 or j == 1 or i == j:
        return 1
    else:
        return Yanghui_Triangle(i - 1,j - 1) + Yanghui_Triangle(i - 1,j)

if __name__ == '__main__':
    line = int(input('Input the line of Yanghui triangle:'))
    for i in range(1, line + 1):
        print(' '*(line - i),end="")
        for j in range(1, i + 1):            
            print('%3d' %Yanghui_Triangle(i, j), end=" ")
        print()