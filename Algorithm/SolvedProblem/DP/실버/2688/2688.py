import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    dp = [[0] * 10 for _ in range(n + 1)]
    dp[1] = [1] * 10
    for i in range(2, n + 1):
        for j in range(10):
            dp[i][j] = sum(dp[i - 1][:j + 1])

    print(sum(dp[-1]))
