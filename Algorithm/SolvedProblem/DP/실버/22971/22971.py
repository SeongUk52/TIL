n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] += dp[j]
            dp[i] %= 998244353

print(*dp)
