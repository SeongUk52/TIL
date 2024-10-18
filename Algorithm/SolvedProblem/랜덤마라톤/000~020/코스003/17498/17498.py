import sys
input = sys.stdin.readline

n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for a in range(1, n):
    for b in range(m):
        ll = []
        for i in range(max(0, a - d), a):
            gap = a - i
            for j in range(max(0, b - d + gap), min(m, b + d - gap + 1)):
                ll.append(dp[i][j] + graph[i][j] * graph[a][b])
        dp[a][b] = max(ll)

print(max(dp[-1]))
