n, m = map(int, input().split())

dp = [list(map(int, input())) for _ in range(n)]


for i in range(1, n):
    for j in range(1, m):
        if dp[i][j] != 0:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

result = 0
for i in dp:
    temp = max(i)
    if temp > result:
        result = temp

print(result ** 2)