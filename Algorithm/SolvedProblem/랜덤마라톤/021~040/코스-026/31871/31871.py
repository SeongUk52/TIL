import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
M = int(data[1])
ans = -1

adj_list = [[] for _ in range(N + 1)]
edge_map = defaultdict(lambda: defaultdict(int))
is_visited = [False] * (N + 1)

for i in range(M):
    u, v, d = map(int, data[i + 2].split())
    if u == v:
        continue
    edge_map[u][v] = max(edge_map[u][v], d)

for u in range(N + 1):
    for v, d in edge_map[u].items():
        adj_list[u].append((v, d))

def dfs(node, dist, count):
    global ans
    if node == 0 and count == N + 1:
        ans = max(ans, dist)
        return
    for next_node, next_dist in adj_list[node]:
        if is_visited[next_node]:
            continue
        is_visited[next_node] = True
        dfs(next_node, dist + next_dist, count + 1)
        is_visited[next_node] = False

dfs(0, 0, 0)
print(ans)
