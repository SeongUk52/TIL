v, e = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(e)]
graph.sort(key=lambda x: x[2])

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
    if treeEdges == v - 1:
        break
    a, b, wt = graph.pop(0)
    if find(a) != find(b):
        union(a, b)
        mst.append((a, b))
        mstCost += wt
        treeEdges += 1
print(mstCost)
