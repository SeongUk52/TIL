from collections import deque

def bfs(n):
    q = deque()
    visited[n] = 0
    q.append((n, 0))
    global cnt
    global k
    while q:
        v, depth = q.popleft()
        if v == k:
            cnt += 1
        if v < k:
            if visited[v * 2] >= depth +1:
                visited[v * 2] = depth + 1
                q.append((v * 2, depth + 1))
            if visited[v + 1] >= depth + 1:
                visited[v + 1] = depth + 1
                q.append((v + 1, depth + 1))
        if v > 0:
            if visited[v - 1] >= depth + 1:
                visited[v - 1] = depth + 1
                q.append((v - 1, depth + 1))

n, k = map(int, input().split())
visited = [100000] * max(n + 1, (k * 2 + 2))
cnt = 0
bfs(n)
print(visited[k])
print(cnt)