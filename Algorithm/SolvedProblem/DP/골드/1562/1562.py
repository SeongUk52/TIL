import sys
input = sys.stdin.readline
n = int(input())
MOD = 10**9
DP = [[[0]*(1<<10) for _ in range(10)] for _ in range(n+1)]

for k in range(10):
    DP[1][k][1<<k] = 1

for i in range(1, n):
    for j in range(10):
        for b in range(1<<10):
            if j < 9:
                DP[i+1][j+1][b | (1<<(j+1))] = (DP[i+1][j+1][b | (1<<(j+1))] + DP[i][j][b]) % MOD
            if j > 0:
                DP[i+1][j-1][b | (1<<(j-1))] = (DP[i+1][j-1][b | (1<<(j-1))] + DP[i][j][b]) % MOD

total = sum(DP[n][k][(1<<10)-1] for k in range(1, 10)) % MOD
print(total)