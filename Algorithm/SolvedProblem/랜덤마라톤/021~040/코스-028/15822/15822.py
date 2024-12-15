import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))
B = list(map(int, data[N+1:2*N+1]))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[1][i] = dp[1][i - 1] + (A[0] - B[i - 1]) ** 2

for i in range(2, N + 1):
    dp[i][1] = dp[i - 1][1] + (A[i - 1] - B[0]) ** 2
    for j in range(2, N + 1):
        v = (A[i - 1] - B[j - 1]) ** 2
        dp[i][j] = min(dp[i][j - 1] + v, dp[i - 1][j - 1] + v, dp[i - 1][j] + v)

print(dp[N][N])