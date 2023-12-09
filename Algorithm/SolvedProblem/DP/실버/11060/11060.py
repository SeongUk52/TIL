n = int(input())

arr = list(map(int, input().split()))

dp = [-1] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if dp[j] == -1:
            continue
        if dp[i] > dp[j] + 1 or dp[i] == -1:
            if arr[j] >= i - j:
                dp[i] = dp[j] + 1

print(dp[-1])
