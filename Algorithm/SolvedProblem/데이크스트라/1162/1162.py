import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    global k
    dists = {j:{i: float('infinity') for i in road} for j in range(k + 1)}
    for i in range(k + 1):
        dists[i][1] = 0
    q = [(0,1,0)]
    while q:
        cd, cv, pave = heapq.heappop(q)

        if cd > dists[pave][cv]:
            continue

        for nv, wt in road[cv].items():
            dist = cd + wt
            if dist < dists[pave][nv]:
                for i in range(pave, k + 1):
                    if dists[i][nv] > dist:
                        dists[i][nv] = dist
                heapq.heappush(q,(dist,nv,pave))

        if pave < k:
            for nv in pavedRoad[cv]:
                dist = cd
                if dist < dists[pave + 1][nv]:
                    for i in range(pave + 1, k + 1):
                        if dists[i][nv] > dist:
                            dists[i][nv] = dist
                    heapq.heappush(q,(dist, nv, pave + 1))
    return dists


n, m, k = map(int, input().split())
road = {i: {} for i in range(n + 1)}
pavedRoad = {i:[] for i in range(n + 1)}

for _ in range(m):
    a, b, c = map(int, input().split())
    if b in road[a]:
        if road[a][b] <= c:
            continue
    road[a][b] = c
    pavedRoad[a].append(b)
    road[b][a] = c
    pavedRoad[b].append(a)
print(dijkstra()[k][n])