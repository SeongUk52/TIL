n = int(input())
arr = list(map(int,input().split()))
dp = [0] * n

for k in range(n):
    dp[k] = 1
    for i in range(k):
        if arr[i] > arr[k]:
            dp[k] = max(dp[k], dp[i] + 1)
print(max(dp))