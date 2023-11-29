n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for row in range(n):
    for col in range(n):
        for preRow in range(row):
            if graph[preRow][col] == row - preRow:
                dp[row][col] += dp[preRow][col]

        for preCol in range(col):
            if graph[row][preCol] == col - preCol:
                dp[row][col] += dp[row][preCol]

print(dp[-1][-1])
