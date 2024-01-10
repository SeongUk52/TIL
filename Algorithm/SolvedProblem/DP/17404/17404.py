MAX = 1000 * 1000 + 1

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

ans = MAX

for start in range(3):
    dp = [[0] * 3 for _ in range(n)]
    for i in range(3):
        if i == start:
            dp[0][start] = arr[0][start]
        else:
            dp[0][i] = MAX

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

    for i in range(3):
        if i == start:
            continue
        ans = min(ans, dp[n - 1][i])

print(ans)
