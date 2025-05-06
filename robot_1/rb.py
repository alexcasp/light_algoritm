x = 3
y = 4
P = [[y] * 0 for i in range(x)]
for i in range(x):
    P[i][0] = 1
for j in range(y):
    P[y][0] = 1
for i in range(1, x):
    for j in range(1, y):
        P[i][j] = P[i][j - 1] + P[i - 1][j] + P[i - 1][j - 1]

for line in P:
    print(line)
print(P[x - 1][y - 1])