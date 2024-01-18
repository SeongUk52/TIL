n = int(input())

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1_000_000_007

print(dp[-1])
