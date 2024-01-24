arr = list(map(int, input().rstrip()))

aLen = len(arr)

dp = [0] * (aLen + 1)
dp[0] = 1
dp[1] = 1

if arr[0] == 0:
    print(0)
else:
    for i in range(2, aLen + 1):
        if arr[i - 1] > 0:
            dp[i] += dp[i - 1]
        if 10 <= arr[i - 1] + arr[i - 2] * 10 <= 26:
            dp[i] += dp[i - 2]
    print(dp[aLen] % 1000000)