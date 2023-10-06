import heapq
import sys
input = sys.stdin.readline

keyRow = [1, -1, 0, 0]
keyCol = [0, 0, 1, -1]


def dijkstra():
    dists = [[float('infinity')] * n for _ in range(n)]
    dists[0][0] = graph[0][0]
    pq = [(graph[0][0], 0, 0)]
    while pq:
        cd, cRow, cCol = heapq.heappop(pq)
        if cd > dists[cRow][cCol]:
            continue
        for i in range(4):
            newRow = cRow + keyRow[i]
            newCol = cCol + keyCol[i]
            if 0 <= newRow < n and 0 <= newCol < n:
                dist = cd + graph[newRow][newCol]
                if dist < dists[newRow][newCol]:
                    dists[newRow][newCol] = dist
                    heapq.heappush(pq,(dist, newRow, newCol))

    return dists


cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    print("Problem " + str(cnt) + ": " + str(dijkstra()[-1][-1]))
