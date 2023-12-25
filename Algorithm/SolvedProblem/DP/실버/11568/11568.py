n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if dp[j] >= dp[i]:
            if arr[i] > arr[j]:
                dp[i] = dp[j] + 1

print(max(dp))