if __name__ == '__main__':
    str_list1 = []
    str1 = input("Input a string:")
    str2 = input("Input a string:")
    str3 = input("Input a string:")
    str_list1.extend([str1, str2, str3])
    print(str_list1)
    str_list1.sort()
    print(str_list1)