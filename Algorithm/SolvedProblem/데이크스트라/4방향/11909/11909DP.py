n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    wt = arr[0][i] - arr[0][i-1] + 1
    if wt < 0:
        wt = 0
    dp[0][i] = dp[0][i - 1] + wt
    wt = arr[i][0] - arr[i - 1][0] + 1
    if wt < 0:
        wt = 0
    dp[i][0] = dp[i - 1][0] + wt

for i in range(1,n):
    for j in range(1,n):
        wt1 = arr[i][j] - arr[i][j - 1] + 1
        if wt1 < 0:
            wt1 = 0
        wt2 = arr[i][j] - arr[i - 1][j] + 1
        if wt2 < 0:
            wt2 = 0
        dp[i][j] = min((dp[i][j - 1] + wt1), (dp[i - 1][j] + wt2))

print(dp[-1][-1])