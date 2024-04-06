if __name__ == '__main__':
    divisor_num = int(input("Input a odd number:"))
    dividend_num = 9
    count = 1
    while 1:
        if dividend_num % divisor_num == 0:
            break
        else:
            dividend_num = dividend_num * 10 + 9
            count += 1
    print("%d个9除以%d的结果为整数" %(count, divisor_num))
    print("%d / %d = %d" %(dividend_num, divisor_num, dividend_num / divisor_num))