dp = [1] * 251
dp[2] = 3
for i in range(3, 251):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

while True:
    try:
        print(dp[int(input())])
    except:
        break
