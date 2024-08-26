import sys

n, m = map(int, sys.stdin.readline().split())
dp = [[0] * (m + 2) for _ in range(n + 2)]
dp[1][1] = 1
holl = [[False] * (m + 2) for _ in range(n + 2)]

for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    holl[x][y] = True

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if j == i == 1:
            continue
        if holl[j][i]:
            continue
        if i % 2 == 1:
            dp[j][i] = (dp[j - 1][i] + dp[j - 1][i - 1] + dp[j][i - 1]) % (10 ** 9 + 7)
        else:
            dp[j][i] = (dp[j - 1][i] + dp[j][i - 1] + dp[j + 1][i - 1]) % (10 ** 9 + 7)

print(dp[n][m])
