n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = (2 * i - 1) * dp[i - 1] % 1000000009
print(dp[-1])
