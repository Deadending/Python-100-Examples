if __name__ == '__main__':
    file_path = r"D:\Coding\Python-100-Examples\100Examples\test.txt"
    string = input('Input a string:')
    string = string.upper()
    with open(file_path, 'a', encoding= 'utf-8') as f:
        f.write(string + '\n')
    with open(file_path, 'r', encoding= 'utf-8') as f:
        print(f.read())