if __name__ == '__main__':
    a = 0x77
    b = a & 3
    print('a & b = %d' % (a & b))
    b &= 7
    print('a & b = %d' % (a & b))