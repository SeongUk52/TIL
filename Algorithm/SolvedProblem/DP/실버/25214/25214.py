n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
min = arr[0]

for i in range(1, n):
    if arr[i] < min:
        min = arr[i]
    dp[i] = max(dp[i - 1], arr[i] - min)

print(*dp)