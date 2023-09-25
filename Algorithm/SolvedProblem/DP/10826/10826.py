n = int(input())
if n == 0:
    print(0)
    exit()
if n <= 2:
    print(1)
    exit()
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[-1])