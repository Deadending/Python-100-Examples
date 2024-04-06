def Sum(num):
    sum = 0
    if num % 2 == 0:
        for i in range(2, num + 1, 2):
            sum += 1.0 / i
    else:
        for i in range(1, num + 1, 2):
            sum += 1.0 / i
    return sum

if __name__ == '__main__':
    n = int(input("Input a number:"))
    sum = Sum(n)
    print(sum)