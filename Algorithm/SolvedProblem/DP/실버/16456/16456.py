n = int(input())

dp = [1] * 50001

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 3]) % 1000000009

print(dp[n])