import heapq

def dijkstra() :
    keyRow = [1, -1, 0 ,0]
    keyCol = [0, 0, 1, -1]
    dists = [[float('infinity')] * m for _ in range(n)]
    dists[row1][col1] = 0
    q = [(0, row1, col1)]

    while q:
        cd, cRow, cCol = heapq.heappop(q)

        if cd > dists[cRow][cCol]:
            continue

        for i in range(4):
            newRow = cRow + keyRow[i]
            newCol = cCol + keyCol[i]

            if 0 <= newRow < n and 0 <= newCol < m:
                if graph[newRow][newCol] == '0' or graph[newRow][newCol] == '*':
                    wt = 0
                else:
                    wt = 1

                dist = wt + cd
                if dist < dists[newRow][newCol]:
                    dists[newRow][newCol] = dist
                    heapq.heappush(q,(dist, newRow, newCol))
    return dists



n, m = map(int, input().split())
row1, col1, row2, col2 = map(int, input().split())
row1 -= 1
col1 -= 1
row2 -= 1
col2 -= 1

graph = [list(input()) for _ in range(n)]

print(dijkstra()[row2][col2])