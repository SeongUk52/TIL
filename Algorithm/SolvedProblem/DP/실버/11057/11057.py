n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = i + 1

for i in range(2, n + 1):
    suma = 0
    for j in range(10):
        suma += dp[i - 1][j]
        dp[i][j] = suma

print(dp[n][9] % 10007)