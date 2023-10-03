import heapq
import sys

input = sys.stdin.readline


def dijkstra(v):
    dists = {i: float('infinity') for i in graph}
    dists[v] = 0
    pq = [(0, v)]
    while pq:
        cd, cv = heapq.heappop(pq)
        if cd > dists[cv]:
            continue
        for nv, wt in graph[cv].items():
            dist = wt + cd
            if dist < dists[nv]:
                dists[nv] = dist
                heapq.heappush(pq, (dist, nv))
    return dists


def getable(dists):
    suma = 0
    for i in range(1, n + 1):
        if dists[i] <= m:
            suma += t[i]
    return suma


n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))
graph = {i: {} for i in range(n + 1)}
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l
maxi = 0
for i in range(1, n + 1):
    tt = getable(dijkstra(i))
    if tt > maxi:
        maxi = tt
print(maxi)
