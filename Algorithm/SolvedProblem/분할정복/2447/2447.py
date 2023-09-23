import math


def star(m, center):
    if m == 0:
        return
    size = 3 ** (m - 1) // 2
    for i in range(center[0] - size - 1, center[0] + size):
        for j in range(center[1] - size - 1, center[1] + size):
            graph[i][j] = " "
    gap = size * 2 + 1
    for i in range(8):
        star(m - 1, (center[0] + gap * keyRow[i], center[1] + gap * keyCol[i] ))


keyRow = [-1, -1, -1, 0, 0, 1, 1, 1]
keyCol = [-1, 0, 1, -1, 1, -1, 0, 1]
n = int(input())
m = int(round(math.log(n, 3),0))
graph = [["*"] * n for _ in range(n)]
star(m, (n // 2 + 1, n // 2 + 1))
for i in graph:
    print(*i,sep='')
