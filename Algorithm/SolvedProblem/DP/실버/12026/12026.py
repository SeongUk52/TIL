import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input().strip())
blocks = list(input().strip())
dp = [INF] * n
dp[0] = 0

def getPrev(block):
    if block == "O":
        return "B"
    elif block == "J":
        return "O"
    elif block == "B":
        return "J"

for i in range(1, n):
    for j in range(i):
        prev = getPrev(blocks[i])
        if blocks[j] == prev:
            jump_cost = (i - j) ** 2
            dp[i] = min(dp[i], dp[j] + jump_cost)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])