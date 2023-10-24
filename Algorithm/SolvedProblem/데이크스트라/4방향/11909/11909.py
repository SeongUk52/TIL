import heapq
import sys
input = sys.stdin.readline

keyRow = [1, 0]
keyCol = [0, 1]
def dijkstra():
    global n
    q = [(0,0,0)]
    dists = [[float('infinity')] * n for _ in range(n)]
    dists[0][0] = 0
    while q:
        cd, cRow, cCol = heapq.heappop(q)

        if dists[cRow][cCol] < cd:
            continue

        for i in range(2):
            newRow = cRow + keyRow[i]
            newCol = cCol + keyCol[i]

            if 0 <= newRow < n and 0 <= newCol < n:
                wt = arr[newRow][newCol] - arr[cRow][cCol] + 1
                if wt < 0:
                    wt = 0
                dist = wt + cd
                if dist < dists[newRow][newCol]:
                    dists[newRow][newCol] = dist
                    heapq.heappush(q,(dist, newRow, newCol))
    return dists


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(dijkstra()[-1][-1])
