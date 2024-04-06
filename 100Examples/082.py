def oct2dec(num):
    num_dec = 0
    for i in range(len(num)):
        num_dec += 8 ** i * int(num[len(num) - 1 - i])
    return num_dec

if __name__ == '__main__':
    num_oct = input("Input a octal number:")
    num_dec = oct2dec(num_oct)
    print("八进制数", num_oct, "转换为十进制数为:", num_dec)
