n = int(input())
dp = [i for i in range(n + 1)]
for i in range(1, n + 1):
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)
    if i >= 7:
        dp[i] = min(dp[i], dp[i - 7] + 1)
print(dp[-1])
