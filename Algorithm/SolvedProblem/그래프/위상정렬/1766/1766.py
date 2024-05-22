import heapq, sys

n, m = map(int, input().split())
ind = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
q = []
result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1

for i in range(1, n + 1):
    if ind[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    result.append(now)
    for i in graph[now]:
        ind[i] -= 1
        if ind[i] == 0:
            heapq.heappush(q, i)

print(*result)
