import sys
input = sys.stdin.readline
v = int(input())
X = []
Y = []
Z = []
for i in range(v):
    x,y,z = map(int,input().split())
    X.append((x,i))
    Y.append((y,i))
    Z.append((z,i))
X.sort(); Y.sort(); Z.sort()

graph = []
for i in range(v-1):
     graph.append((X[i][1],X[i+1][1],abs(X[i+1][0]-X[i][0])))
     graph.append((Y[i][1],Y[i+1][1],abs(Y[i+1][0]-Y[i][0])))
     graph.append((Z[i][1],Z[i+1][1],abs(Z[i+1][0]-Z[i][0])))
graph.sort(key=lambda x: x[2],reverse=True)

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
    a, b, wt = graph.pop()
    if find(a) != find(b):
        union(a, b)
        mstCost += wt
        treeEdges += 1
print(mstCost)
