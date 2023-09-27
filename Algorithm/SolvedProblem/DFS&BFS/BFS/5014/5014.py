from collections import deque

f, s, g, u, d = map(int, input().split())
q = deque()
visited = [False] * (f + 1)
flag = True
visited[s] = True
q.append((s,0))
while q and not(u == 0 and d == 0):
    now = q.popleft()
    if now[0] == g:
        print(now[1])
        flag = False
        break
    if now[0] + u <= f and not visited[now[0] + u]:
        q.append((now[0] + u,now[1] + 1))
        visited[now[0] + u] = True
    if now[0] - d > 0 and not visited[now[0] - d]:
        q.append((now[0] - d,now[1] + 1))
        visited[now[0] - d] = True
if flag:
    print("use the stairs")