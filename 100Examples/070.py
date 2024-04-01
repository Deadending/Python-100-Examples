def len_of_string(string):
    sum = 0
    for s in string:
        sum += 1
    return sum

if __name__ =='__main__':
    s = input('Input a string:')
    length = len_of_string(s)
    print("The string has %d characters." %length)