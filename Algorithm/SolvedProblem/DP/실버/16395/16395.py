n, k = map(int, input().split())

dp = [[1] for _ in range(n)]

dp[1] += [1]

for i in range(2, n):
    for j in range(i - 1):
        dp[i].append(dp[i - 1][j] + dp[i - 1][j + 1])
    dp[i].append(1)


print(dp[n - 1][k - 1])