import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    for neighbor in sorted(graph[node], reverse=True):
        if visited[neighbor] == -1:
            visited[neighbor] = visited[node] + 1
            dfs(neighbor)

visited[r] = 0
dfs(r)

print(*visited[1:], sep='\n')