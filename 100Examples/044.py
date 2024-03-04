X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = []
for i in range(3):
    result.append([])

for i in range(3):
    for j in range(3):
        result[i].append(X[i][j] + Y[i][j])

for r in result:
    print(r)