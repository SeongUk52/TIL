import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

graph = []
for i in range(e):
    a, b, wt = map(int,input().split())
    heapq.heappush(graph,(wt,a,b))

mst = []
p = [0]

for i in range(1, v + 1):
    p.append(i)


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1


treeEdges = 0
mstCost = 0
while True:
    if treeEdges == v - 2:
        break
    wt, a, b = heapq.heappop(graph)
    if find(a) != find(b):
        union(a, b)
        mst.append((a, b, wt))
        mstCost += wt
        treeEdges += 1

print(mstCost)
