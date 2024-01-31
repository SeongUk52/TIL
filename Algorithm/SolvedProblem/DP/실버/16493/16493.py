day, page = map(int, input().split())
d = [0]
p = [0]
result = 0
dp = [[0] * 201 for _ in range(21)]

for i in range(page):
    a, b = map(int, input().split())
    d.append(a)
    p.append(b)

for i in range(1, page + 1):
    for j in range(day, 0, -1):
        if j - d[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - d[i]] + p[i])
        else:
            dp[i][j] = dp[i - 1][j]
        result = max(result, dp[i][j])

print(result)
