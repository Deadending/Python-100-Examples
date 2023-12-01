def Hello():
    print('Hello World!')
def HelloAgain(n):
    for i in range(n):
        Hello()

if __name__ == '__main__':
    HelloAgain(3)