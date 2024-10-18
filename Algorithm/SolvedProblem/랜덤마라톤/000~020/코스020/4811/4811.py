dp = [[0] * 31 for _ in range(31)]

for h in range(31):
    for w in range(31):
        if h > w:
            continue
        if h == 0:
            dp[w][h] = 1
        else:
            dp[w][h] = dp[w - 1][h] + dp[w][h - 1]

for _ in range(1000):
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])
