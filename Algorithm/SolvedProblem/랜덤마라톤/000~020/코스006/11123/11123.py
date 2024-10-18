import sys
sys.setrecursionlimit(10 ** 4)

keyRow = [1, -1, 0, 0]
keyCol = [0, 0, 1, -1]


def count_sheep():
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == "#":
                cnt += 1
                dfs(i, j, visited)
    return cnt


def dfs(r, c, visited):
    visited[r][c] = True
    for i in range(4):
        nr = r + keyRow[i]
        nc = c + keyCol[i]
        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and graph[nr][nc] == '#':
            dfs(nr, nc, visited)


for _ in range(int(input())):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    print(count_sheep())
