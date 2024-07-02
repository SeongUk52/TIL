n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * m for _ in range(n)] for _ in range(3)]

for i in range(3):
    for j in range(m):
        dp[i][0][j] = graph[0][j]

for i in range(1, n):
    dp[1][i][0] = dp[2][i - 1][0] + graph[i][0]
    dp[2][i][0] = min(dp[0][i - 1][1], dp[1][i - 1][1]) + graph[i][0]
    for j in range(1, m - 1):
        dp[0][i][j] = min(dp[1][i - 1][j - 1], dp[2][i - 1][j - 1]) + graph[i][j]
        dp[1][i][j] = min(dp[0][i - 1][j], dp[2][i - 1][j]) + graph[i][j]
        dp[2][i][j] = min(dp[0][i - 1][j + 1], dp[1][i - 1][j + 1]) + graph[i][j]
    dp[0][i][m - 1] = min(dp[1][i - 1][m - 2], dp[2][i - 1][m - 2]) + graph[i][m - 1]
    dp[1][i][m - 1] = dp[0][i - 1][m - 1] + graph[i][m - 1]

result = min(dp[0][n - 1][1:])
result = min(result, min(dp[1][n - 1]))
result = min(result, min(dp[2][n - 1][:m - 1]))
print(result)
