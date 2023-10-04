import heapq
def dijkstra(v):
    dists = {i:float("infinity") for i in graph}
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
                heapq.heappush(pq,(dist, nv))
    return dists

n, m = map(int,input().split())
graph = { i: {} for i in range(n + 1)}
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
s, t = map(int, input().split())
print(dijkstra(s)[t])