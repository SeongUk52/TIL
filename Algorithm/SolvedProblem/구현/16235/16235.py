import sys
input = sys.stdin.readline
dirR = [-1, -1, -1, 0, 0, 1, 1, 1]
dirC = [-1, 0, 1, -1, 1, -1, 0, 1]
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
trees = [[[]for _ in range(n)] for _ in range(n)]
nuts = [[5] * n for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

for _ in range(k):
    birth = []
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                growth = []
                trees[i][j].sort()
                death = 0
                for age in trees[i][j]:
                    if nuts[i][j] >= age:
                        nuts[i][j] -= age
                        if (age + 1) % 5 == 0:
                            birth.append((i, j))
                        growth.append(age + 1)
                    else:
                        death += age // 2
                nuts[i][j] += death
                trees[i][j] = growth
    while birth:
        x, y = birth.pop()
        for i in range(8):
            newR = x + dirR[i]
            newC = y + dirC[i]
            if 0 <= newR < n and 0 <= newC < n:
                trees[newR][newC].append(1)

    for i in range(n):
        for j in range(n):
            nuts[i][j] += a[i][j]
cnt = 0
for i in range(n):
    for j in range(n):
        if trees[i][j]:
            cnt += len(trees[i][j])

print(cnt)
