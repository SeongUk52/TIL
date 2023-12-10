dp = [1] * 68

dp[2] = 2
dp[3] = 4

for i in range(4, 68):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

tc = int(input())

for i in range(tc):
    print(dp[int(input())])