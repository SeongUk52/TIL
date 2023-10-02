import heapq
import sys
input = sys.stdin.readline

def dijkstra(v):
    distances = {i: float('infinity') for i in graph}
    distances[v] = 0
    pq = [(0, v)]
    while pq:
        cd, cv = heapq.heappop(pq)
        if cd > distances[cv]:
            continue
        for nv, wt in graph[cv].items():
            dist = cd + wt
            if dist < distances[nv]:
                distances[nv] = dist
                heapq.heappush(pq, (dist, nv))

    return distances


tc = int(input())

for _ in range(tc):
    n, d, c = map(int, input().split())
    graph = {i: {} for i in range(n + 1)}
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b][a] = s
    dists = dijkstra(c)
    cnt = 0
    max = 0
    for i in dists.values():
        if i == float('infinity'):
            continue
        cnt += 1
        if i > max:
            max = i
    print(cnt, max)
