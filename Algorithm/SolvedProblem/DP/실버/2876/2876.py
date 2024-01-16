n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(6)]

for i in range(n):
    dp[arr[i][0]][i + 1] = dp[arr[i][0]][i] + 1
    dp[arr[i][1]][i + 1] = dp[arr[i][1]][i] + 1

print(max(map(max, dp)), list(map(max, dp)).index(max(map(max, dp))))