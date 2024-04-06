if __name__ == '__main__':
    original_num = input('Input a four-figit number:')
    encrypted_num = 0
    encrypted_num_list = []
    for i in range(4):
        encrypted_num_list.append((int(original_num[i]) + 5) % 10)
    encrypted_num_list[0], encrypted_num_list[3] = encrypted_num_list[3], encrypted_num_list[0]
    encrypted_num_list[1], encrypted_num_list[2] = encrypted_num_list[2], encrypted_num_list[1]
    for i in range(4):
        encrypted_num += encrypted_num_list[i] * 10 ** (3 - i)
    print(encrypted_num)