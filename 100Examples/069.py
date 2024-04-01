if __name__ == '__main__':
    N = int(input("Input the num of people:"))
    people = [i + 1 for i in range(N)]
    index = 1
    while len(people) > 1:
        if index % 3 == 0:
            people.pop(0)
        else:
            people.insert(len(people), people.pop(0))
        index += 1
    print(people)