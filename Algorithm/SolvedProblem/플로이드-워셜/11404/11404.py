n = int(input())
m = int(input())

graph = [[float('infinity')] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] == float('infinity'):
            graph[i][j] = 0

for i in graph:
    print(*i)
