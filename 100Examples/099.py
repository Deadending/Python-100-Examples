if __name__ == '__main__':
    with open('100Examples/097test.txt', 'r', encoding='utf-8') as f:
        a = f.read()
    with open('100Examples/test.txt', 'r', encoding='utf-8') as f:
        b = f.read()
    file_path = r"D:\Coding\Python-100-Examples\100Examples\099test.txt"
    with open(file_path, 'a+', encoding='utf-8') as f:
        c = list(a+b)
        c.sort()
        sorted_string = ''.join(c)
        f.write(sorted_string)