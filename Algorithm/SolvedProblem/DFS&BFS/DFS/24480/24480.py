import sys
sys.setrecursionlimit(100000)

n, m, r = map(int, input().split())

graph = {i: [] for i in range(n + 1)}

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph.values():
    i.sort(reverse=True)
cnt = 1
visited = [0] * n


def dfs(now):
    global cnt
    visited[now - 1] = cnt
    for i in graph[now]:
        if visited[i - 1] == 0:
            cnt += 1
            dfs(i)


dfs(r)

print(*visited, sep="\n")
