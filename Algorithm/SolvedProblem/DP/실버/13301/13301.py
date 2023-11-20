n = int(input())

dp = [0] * (n + 1)
result = [0] * (n + 1)

dp[1] = 1
result[1] = 4

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    result[i] = 2 * dp[i] + result[i - 1]

print(result[-1])