import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
ret = []

for _ in range(m):
    a, b = map(int, input().split())
    g[b].append(a)


def bfs(i):
    d = deque([i])
    visit = [0] * (n + 1)
    visit[i] = 1
    cnt = 1
    while d:
        i = d.popleft()
        for j in g[i]:
            if not visit[j]:
                d.append(j)
                visit[j] = 1
                cnt += 1
    return cnt


max_cnt = 1
for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        ret = [i]
    elif cnt == max_cnt:
        ret.append(i)

print(*ret)
