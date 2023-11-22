import copy
from collections import deque

KEYROW = [1, -1, 0, 0]
KEYCOL = [0, 0, 1, -1]

def bt(comb, srow, scol):
    if len(comb) == 3:
        wall.append(comb[:])
        return

    for i in range(srow, n):
        for j in range(scol if i == srow else 0, m):
            if graph[i][j] == 0:
                comb.append([i, j])
                if j < m - 1:
                    bt(comb, i, j + 1)
                else:
                    bt(comb, i + 1, 0)
                comb.pop()


def bfs(temp):
    q = deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append([i,j])
    safeZone = 0
    while q:
        cRow, cCol = q.popleft()

        for i in range(4):
            newRow = cRow + KEYROW[i]
            newCol = cCol + KEYCOL[i]
            if 0 <= newRow < n and 0 <= newCol < m:
                if temp[newRow][newCol] == 0:
                    temp[newRow][newCol] = 2
                    q.append([newRow, newCol])
    for i in temp:
        for j in i:
            if j == 0:
                safeZone += 1
    return safeZone


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
wall = []
bt([], 0, 0)
result = 0
for i in wall:
    tempGraph = copy.deepcopy(graph)
    tempGraph[i[0][0]][i[0][1]] = 1
    tempGraph[i[1][0]][i[1][1]] = 1
    tempGraph[i[2][0]][i[2][1]] = 1
    tempRe = bfs(tempGraph)

    if tempRe > result:
        result = tempRe

print(result)