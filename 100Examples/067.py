def find_max(array):
    max = 0
    for i in range(1, len(array)):        
        p = i
        if array[p] > array[max]:
            max = p
    return max

def find_min(array):
    min = 0
    for i in range(1, len(array)):        
        p = i
        if array[p] < array[min]:
            min = p
    return min

if __name__ == '__main__':
    N = int(input('Input the length of array:'))
    array = []
    for i in range(N):
        array.append(int(input('Input a number:')))
    print("交换前：", end='')
    print(array)
    max_index = find_max(array)
    min_index = find_min(array)
    # 如果第一个值是最小值，先交换最小值
    if min_index == 0:
            # 如果第一个值是最小值，最后一个值是最大值，直接首尾交换
        if  max_index == N - 1:
            array[0], array[N - 1] = array[N - 1], array[0]
        else:
            array[N - 1], array[min_index] = array[min_index], array[N - 1]
            array[0], array[max_index] = array[max_index], array[0]
    # 其他情况直接交换
    else:
        array[0], array[max_index] = array[max_index], array[0]
        array[N - 1], array[min_index] = array[min_index], array[N - 1]
    print("交换后：", end='')
    print(array)