n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    a = int(i / 2)
    b = i - a
    dp[i] = dp[a] + dp[b] + a * b

print(dp[-1])
