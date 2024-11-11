import sys

N = int(input())
cards = sys.stdin.readline().split()
M, K = map(int, sys.stdin.readline().split())
board = [[] for _ in range(M + 1)]

for _ in range(K):
    i, j, c = sys.stdin.readline().split()
    board[int(i)].append((int(j), c))
    board[int(j)].append((int(i), c))

dp = [[0 for _ in range(M + 1)] for _ in range(N+1)]

for i in range(N-1, -1, -1):
    current_card = cards[i]
    for j in range(M, 0, -1):
        temp = 0
        for k in board[j]:
            node = k[0]
            vertex = k[1]
            temp = max(dp[i+1][node] + (10 if vertex == current_card else 0), temp)
        dp[i][j] = temp
print(dp[0][1])
