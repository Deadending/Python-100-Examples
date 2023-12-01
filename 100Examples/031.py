letter = input('Please input a upper letter:')
if letter == 'M':
    print('Monday!')
elif letter == 'T':
    letter = input('Please input another lower letter:')
    if letter == 'u':
        print('Tuesday!')
    elif letter == 'h':
        print('Thursday!')
    else:
        print('Input Error!')
elif letter == 'W':
    print('Wednesday!')
elif letter == 'F':
    print('Friday!')
elif letter == 'S':
    letter = input('Please input another lower letter:')
    if letter == 'a':
        print('Saturday!')
    elif letter == 'u':
        print('Sunday!')
    else:
        print('Input Error!')
else:
    print('Input Error!')

day_T = {'u':'Tuesday',
        'h':'Thursday'}
day_S = {'a':'Saturday',
         'u':'Sunday'}
day = {'M':'Monday',
       'W':'Wednesday',
       'F':'Friday',
       'T':day_T,
       'S':day_S}
letter = day[input('Please input a upper letter:')]
if letter == day_T or letter == day_S:
    print(letter[input('Please input another lower letter:')])
else:
    print(letter)