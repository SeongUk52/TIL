from collections import deque


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
ind = [0] * (n + 1)
q = deque()
basics = []
times = [{i:0 for i in range(n + 1)} for _ in range(n + 1)]

for _ in range(m):
    x, y, k = map(int, input().split())
    for i in range(k):
        graph[y].append(x)
    ind[x] += k

for i in range(1, n + 1):
    if ind[i] == 0:
        q.append(i)
        times[i][i] = 1
        basics.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        ind[i] -= 1
        for j in range(1, n + 1):
            times[i][j] += times[now][j]

        if ind[i] == 0:
            q.append(i)


for i in basics:
    print(i, times[n][i])
