n = int(input())
m = int(input())

dp = [[1] * m for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(i, m):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

print(dp[-1][-1])