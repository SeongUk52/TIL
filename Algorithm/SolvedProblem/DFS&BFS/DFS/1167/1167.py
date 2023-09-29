def dfs(now, total):
    global maxi
    visited[now] = True
    if total > maxi[1]:
        maxi = (now, total)
    for i in graph[now]:
        if not visited[i]:
            dfs(i, total + graph[now][i])

v = int(input())
graph = {i: {} for i in range(1, v + 1)}
for i in range(v):
    inputs = list(map(int, input().split()))
    for j in range((len(inputs) - 2) // 2):
        graph[inputs[0]][inputs[j * 2 + 1]] = inputs[j * 2 + 2]
maxi = (0,0)
visited = [False] * (v + 1)
dfs(1,0)
visited = [False] * (v + 1)
dfs(maxi[0], 0)
print(maxi[1])