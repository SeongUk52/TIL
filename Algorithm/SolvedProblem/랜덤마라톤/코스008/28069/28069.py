n, k = map(int, input().split())
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    m = i + int(i / 2)
    if m <= n:
        dp[m] = min(dp[m], dp[i] + 1)
print("minigimbob" if dp[n] <= k else "water")
