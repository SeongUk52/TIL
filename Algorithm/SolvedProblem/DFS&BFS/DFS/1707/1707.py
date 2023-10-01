import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(start,check):
    global result
    if result == "NO":
        return
    newCheck = check % 2 + 1
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = newCheck
            dfs(i, newCheck)
        else:
            if visited[i] != newCheck:
                result = "NO"

k = int(input())
for _ in range(k):
    v, e = map(int,input().split())
    visited = [0] * (v + 1)
    visited[0], visited[1] = 1, 1
    result = "YES"
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    dfs(1,1)
    for i in range(v + 1):
        if result == "NO":
            break
        if visited[i] == 0:
            dfs(i, 1)
    print(result)
