n = int(input())

dp = [i for i in range(n + 1)]


for i in range(n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)

print(dp[-1])