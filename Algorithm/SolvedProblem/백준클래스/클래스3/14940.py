from collections import deque
import sys
input = sys.stdin.readline

keyRow = [1, -1, 0, 0]
keyCol = [0, 0, 1, -1]


def bfs(goalRow, goalCol):
    visited = [[False] * m for _ in range(n)]
    result = [[0] * m for _ in range(n)]
    visited[goalRow][goalCol] = True
    q = deque()
    q.append((goalRow, goalCol, 0))

    while q:
        nowRow, nowCol, dist = q.popleft()

        result[nowRow][nowCol] = dist

        for i in range(4):
            newRow = nowRow + keyRow[i]
            newCol = nowCol + keyCol[i]

            if (0 <= newRow < n and 0 <= newCol < m and
                    not visited[newRow][newCol] and graph[newRow][newCol] != 0):
                q.append((newRow, newCol, dist + 1))
                visited[newRow][newCol] = True

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                result[i][j] = -1

    return result


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
goalRow, goalCol = 0, 0
for i in range(n):
    if 2 in graph[i]:
        goalRow = i
        goalCol = graph[i].index(2)

result = bfs(goalRow, goalCol)

for i in result:
    print(*i)
