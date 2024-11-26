import sys

sys.setrecursionlimit(10 ** 6)

keyRow, keyCol = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + keyRow[i], y + keyCol[i]
        if 0 <= nx < m + 1 and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 1:
            dfs(nx, ny)


m, n = map(int, input().split())
graph = [[0] * n] + [list(map(int, input())) for _ in range(m)]
visited = [[False] * n for _ in range(m + 1)]

dfs(0, 0)

print("YES" if True in visited[-1] else "NO")
