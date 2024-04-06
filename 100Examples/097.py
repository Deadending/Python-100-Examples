if __name__ == '__main__':
    filename = input('输入文件名：')
    file_path = r"D:\Coding\Python-100-Examples\100Examples\{}.txt".format(filename)
    ch = ''
    while '#' not in ch:
        with open(file_path, 'a', encoding= 'utf-8') as f:
            f.write(ch + '\n')
        ch = input('输入字符串：')