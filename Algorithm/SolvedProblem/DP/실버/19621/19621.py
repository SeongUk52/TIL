n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

dp[1] = arr[0][2]


for i in range(2, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1][2])

print(dp[-1])