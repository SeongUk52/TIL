n, m = map(int ,input().split())

arr = [[0] * (m + 1)]

for i in range(n):
    arr.append([0] + list(map(int,input().split())))


dp = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[j][i] = max(dp[j][i - 1] + arr[j][i], dp[j - 1][i] + arr[j][i])

print(dp[n][m])