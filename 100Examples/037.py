import math

# 冒泡排序
def BubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 选择排序
def SelectSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        # i不是最小数时，交换
        if i != minindex:
            arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr

# 插入排序
def InsertionSort(arr):
    for i in range(len(arr)):
        preindex = i - 1
        current = arr[i]
        while preindex >= 0 and arr[preindex] > current:
            arr[preindex + 1] = arr[preindex]
            preindex -= 1
        arr[preindex + 1] = current
    return arr

# 希尔排序
def ShellSort(arr):
    gap = 1
    while gap < 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
    return arr

# 归并排序
def MergeSort(arr):
    if len(arr) < 2:
        return arr
    middle  = math.floor(len(arr)/2)
    left, right = arr[0 : middle], arr[middle : ]
    return Merge(MergeSort(left), MergeSort(right))

def Merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

# 快速排序
def QuickSort(arr, left = None, right = None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = Partition(arr, left, right)
        QuickSort(arr, left, partitionIndex - 1)
        QuickSort(arr, partitionIndex + 1, right)
    return arr

def Partition(arr, left, right):
    pivot = left 
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            Swap(arr, i, index)
            index += 1
        i += 1
    Swap(arr, pivot, index - 1)
    return index -1 

def Swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    test_list = [5,3,23,67,2,56,45,98,239,9]
    print(InsertionSort(test_list))