import string

def String_Count(s):
    letters = 0
    space = 0
    digit = 0
    others = 0
    for ele in s:
        if ele.isalpha():
            letters += 1
        elif ele.isspace():
            space += 1
        elif ele.isdigit():
            digit += 1
        else:
            others += 1
    return letters,space,digit,others


if __name__ == '__main__':
    s = input("输入一个字符串：")
    (letters,space,digit,others) = String_Count(s)
    print("字母%d个，空格%d个，数字%d个，其他%d个" %(letters,space,digit,others))