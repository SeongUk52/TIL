from collections import deque

n, m = map(int, input().split())
result = [1] * (n + 1)
ind = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1

for i in range(1, n + 1):
    if ind[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        ind[i] -= 1
        if ind[i] == 0:
            q.append(i)
            result[i] += result[now]

print(*result[1:])
