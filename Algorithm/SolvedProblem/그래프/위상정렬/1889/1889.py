from collections import deque

n = int(input())
q = deque()
ind = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(1, n + 1):
    a, b = map(int, input().split())
    graph[i].append(a)
    graph[i].append(b)
    ind[a] += 1
    ind[b] += 1

for i in range(1, n + 1):
    if ind[i] < 2:
        q.append(i)

while q:
    now = q.popleft()
    if visited[now]:
        continue
    visited[now] = True
    for i in graph[now]:
        ind[i] -= 1
        if ind[i] < 2:
            q.append(i)

size = ind.count(2)
result = []
for i in range(1, n + 1):
    if ind[i] == 2:
        result.append(i)

print(size)
if size != 0:
    print(*result)
