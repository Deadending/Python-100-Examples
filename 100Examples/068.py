if __name__ == '__main__':
    m = int(input("Input the number of moves:"))
    n = int(input("Input length of the list:"))
    array = []
    for i in range(n):
        array.append(int(input("Input a number:")))
    print("移动前：", array)
    array = array[n - m: n] + array[0: n - m]
    print("移动后：", array)