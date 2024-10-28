n, m = map(int, input().split())
a = list(map(int, input().split()))
sum = [[0] * n for _ in range(n)]
for i in range(n):
    sum[i][i] = a[i]
for i in range(1, n):
    for j in range(i):
        sum[j][i] = sum[j][i - 1] + a[i]

dp = [[-float('infinity')] * (m + 1) for _ in range(n)]
for i in range(n):
    dp[i][0] = 0

for i in range(n):
    for j in range(i + 1):
        dp[i][1] = max(dp[i][1], sum[j][i])

for k in range(2, m + 1):
    for i in range(n):
        for j in range(i):
            for r in range(j + 1, i + 1):
                dp[i][k] = max(dp[i][k], dp[j][k - 1] + sum[r][i])
maxi = -float('infinity')
for i in range(n):
    maxi = max(maxi, dp[i][m])
print(maxi)
