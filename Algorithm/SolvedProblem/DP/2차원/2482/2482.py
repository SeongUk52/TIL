div_facter = 1000000003

n = int(input())
k = int(input())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][1] = i

for i in range(4, n + 1):
    for j in range(2, k + 1):
        dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % div_facter

print(dp[-1][-1])
