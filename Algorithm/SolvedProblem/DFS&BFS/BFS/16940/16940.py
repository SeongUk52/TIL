from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
cnts = [-1] * (n + 1)
vc = [set() for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
cnts[1] = 0
while q:
    now = q.popleft()
    for i in graph[now]:
        if cnts[i] == -1:
            cnts[i] = cnts[now] + 1
            vc[now].add(i)
            q.append(i)

comp = list(map(int, input().split()))
idx = 1
for i in comp:
    if idx == n:
        break
    cl = len(vc[i])
    c1 = set(comp[idx:idx+cl])
    c2 = vc[i]
    if c1 != c2:
        print(0)
        exit()
    idx += cl

print(1)
