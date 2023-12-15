n = int(input())

arr = [float(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = max(dp[i - 1] * arr[i], arr[i])

print('%0.3f' % max(dp))