a, b, c = ['\0' + input() for _ in range(3)]
dp = [[[0 for _ in range(len(c)+1)] for _ in range(len(b)+1)]
      for _ in range(len(a)+1)]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        for k in range(1, len(c)):
            if a[i] == b[j] == c[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-2][-2][-2])