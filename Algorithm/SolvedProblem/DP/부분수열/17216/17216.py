n = int(input())

arr = list(map(int, input().split()))

dp = arr[:]

for i in range(1, n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])


print(max(dp))