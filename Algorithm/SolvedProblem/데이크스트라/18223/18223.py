import heapq
import sys
def dijkstra(start):
    dists = {i:float('infinity') for i in graph}
    dists[start] = 0
    pq = [(0, start)]
    while pq:
        cd, cv = heapq.heappop(pq)
        if cd > dists[cv]:
            continue
        for nv, wt in graph[cv].items():
            dist = wt + cd
            if dist < dists[nv]:
                dists[nv] = dist
                heapq.heappush(pq,(dist, nv))
    return dists


v, e, p = map(int, input().split())
graph = {i: {} for i in range(v + 1)}
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
dists1 = dijkstra(1)
distsP = dijkstra(p)
if dists1[v] == dists1[p] + distsP[v]:
    print("SAVE HIM")
else:
    print("GOOD BYE")