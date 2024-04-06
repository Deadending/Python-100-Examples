import time
import random

if __name__ == '__main__':
    flag = input('Do you want to play it?(\'y\' or \'n\')')
    while flag == 'y':
        print("随机数生成中...")
        goal_num = random.randint(1,100)
        print("随机数生成完毕！")

        start = time.perf_counter()
        guess_num = int(input('Input your guess:'))
        while guess_num != goal_num:
            if guess_num > goal_num:
                print('Please input a smaller number:')
                guess_num = int(input('Input your guess:'))
            else:
                print('Please input a bigger number:')
                guess_num = int(input('Input your guess:'))
        end = time.perf_counter()
        var = end - start
        print('It tooks your %6.3f s' %var)
        if var < 15:
            print('You are very clever!')
        elif var < 25:
            print('You are normal.')
        else:
            print('You are stupid!')
        flag = input('Do you want to play it again?(\'y\' or \'n\')')