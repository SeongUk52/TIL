from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ind = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
q = deque()
result = []
for i in range(m):
    inputs = list(map(int, input().split()))
    for j in range(1, inputs[0]):
        graph[inputs[j]].append(inputs[j + 1])
        ind[inputs[j + 1]] += 1
for i in range(1, n + 1):
    if ind[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        ind[i] -= 1
        if ind[i] == 0:
            q.append(i)

if len(result) != n:
    print(0)
else:
    print(*result, sep='\n')
