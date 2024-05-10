from collections import deque
import sys
input = sys.stdin.readline


dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]


def bfs():
    visited = [[False] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))

    while q:
        r, c = q.popleft()
        if visited[r][c]:
            continue

        visited[r][c] = True

        for i in range(4):
            newR = r + dirR[i]
            newC = c + dirC[i]
            if 0 <= newR < n and 0 <= newC < m and not visited[newR][newC]:
                if graph[newR][newC] == 0:
                    q.append((newR, newC))
                elif graph[newR][newC] == 1:
                    cnt[newR][newC] += 1

    for i in range(n):
        for j in range(m):
            if cnt[i][j] >= 2:
                graph[i][j] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
goal = [[0] * m for _ in range(n)]

while graph != goal:
    cnt += 1
    bfs()

print(cnt)
