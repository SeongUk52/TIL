from collections import deque

n = int(input())
ind = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
value = [0] * (n + 1)
result = [0] * (n + 1)
q = deque()
for i in range(n):
    inputs = list(map(int, input().split()))
    value[i + 1] = inputs[0]
    ind[i + 1] = len(inputs) - 2
    if ind[i + 1] == 0:
        q.append(i + 1)
        result[i + 1] = value[i + 1]
    for j in inputs[1:-1]:
        graph[j].append(i + 1)


while q:
    now = q.popleft()
    for i in graph[now]:
        ind[i] -= 1
        result[i] = max(result[i], result[now])
        if ind[i] == 0:
            q.append(i)
            result[i] += value[i]

for i in result[1:]:
    print(i)
