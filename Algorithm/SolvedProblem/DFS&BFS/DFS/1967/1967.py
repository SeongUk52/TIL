import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs2(v, suma):
    global maxi
    visited[v] = True
    if suma > maxi[1]:
        maxi = (v, suma)
    for i in graph[v]:
        if not visited[i]:
            dfs2(i, suma + graph[v][i])


maxi = (0, 0)
n = int(input())
if n == 1:
    print(0)
    exit()
graph = {i: {} for i in range(1, n + 1)}
visited = [False] * (n + 1)
for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
dfs2(1, 0)
visited = [False] * (n + 1)
dfs2(maxi[0],0)
print(maxi[1])