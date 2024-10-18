n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * n for _ in range(m)]
dp[0][0] = 1
for i in range(1, n):
    if dp[0][i - 1] == 1 and graph[0][i] == 1:
        dp[0][i] = 1
    else:
        break
for i in range(1, m):
    if dp[i - 1][0] == 1 and graph[i][0] == 1:
        dp[i][0] = 1
    else:
        break
for i in range(1, m):
    for j in range(1, n):
        if graph[i][j] == 1:
            if dp[i - 1][j] == 1 or dp[i][j - 1] == 1:
                dp[i][j] = 1

if dp[-1][-1] == 1:
    print("Yes")
else:
    print("No")
