n = int(input())

dp = [1] * 3


for i in range(1, n):
    temp0 = dp[0]
    temp1 = dp[1]
    temp2 = dp[2]
    dp[0] = temp0 + temp1 + temp2 % 9901
    dp[1] = temp0 + temp2 % 9901
    dp[2] = temp0 + temp1 % 9901

print(sum(dp) % 9901)