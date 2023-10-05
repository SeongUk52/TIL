import heapq
def dijkstra():
    dists = [[float('infinity')] * m for i in range(n)]
    dists[0][0] = 0
    pq = [(0, 0, 0)]
    keyRow = [1,-1,0,0]
    keyCol = [0,0,1,-1]
    while pq:
        cd, cRow, cCol = heapq.heappop(pq)
        if cd > dists[cRow][cCol]:
            continue
        for i in range(4):
            newRow = cRow + keyRow[i]
            newCol = cCol + keyCol[i]
            if 0 <= newRow < n and 0 <= newCol < m:
                dist = graph[newRow][newCol] + cd
                if dist < dists[newRow][newCol]:
                    dists[newRow][newCol] = dist
                    heapq.heappush(pq,(dist, newRow, newCol))
    return dists



m, n = map(int, input().split())
graph = [list(map(int, input())) for i in range(n)]
print(dijkstra()[-1][-1])