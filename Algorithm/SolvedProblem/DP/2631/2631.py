n = int(input())

arr = [int(input()) for _ in range(n)]

dp = [1] * n

for i in range(n):
    for j in range(0, i):
        if arr[i] > arr[j] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

print(n - max(dp))