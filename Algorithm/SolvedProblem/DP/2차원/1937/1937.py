KEYROW = [1, -1, 0, 0]
KEYCOL = [0, 0, 1, -1]

def dfs(i, j):
    global ans
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 1
    for k in range(4):
        newRow = i + KEYROW[k]
        newCol = j + KEYCOL[k]
        if 0 <= newRow < n and 0 <= newCol < n:
            if graph[newRow][newCol] > graph[i][j]:
                cnt = 1
                cnt += dfs(newRow, newCol)
                dp[i][j] = max(dp[i][j], cnt)
                ans = max(ans, dp[i][j])
    return dp[i][j]

ans = 1
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            dfs(i, j)

print(max(map(max, dp)))
