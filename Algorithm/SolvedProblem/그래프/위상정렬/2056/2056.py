from collections import deque

n = int(input())
ind = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
result = [0] * (n + 1)
q = deque()

for i in range(1, n + 1):
    inputs = list(map(int, input().split()))
    time[i] = inputs[0]
    ind[i] = inputs[1]
    if ind[i] == 0:
        q.append(i)
        result[i] = time[i]
    for j in inputs[2:]:
        graph[j].append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        ind[i] -= 1
        result[i] = max(result[i], result[now])
        if ind[i] == 0:
            q.append(i)
            result[i] += time[i]

print(max(result))
