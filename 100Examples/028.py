def Age(n):
    if n == 1:
        return 10
    else:
        return Age(n - 1) + 2
    
print(Age(5))