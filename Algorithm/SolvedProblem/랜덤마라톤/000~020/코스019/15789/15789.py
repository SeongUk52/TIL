from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
c, h, k = map(int, input().split())


def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n+1)]
for a in range(1, n+1):
    for b in graph[a]:
        if find_parent(a, parent) == find_parent(b, parent):
            continue
        else:
            union_parent(a, b, parent)

group = defaultdict(int)
ctp_root, hs_root = -1, -1
for i in range(1, n+1):
    root = find_parent(i, parent)
    group[root] += 1
    if i == c:
        ctp_root = i
    if i == h:
        hs_root = i

ans = group[ctp_root]
for key, val in sorted(group.items(), key=lambda x: x[1], reverse=True):
    if key == hs_root or key == ctp_root:
        continue
    if k <= 0:
        break
    ans += val
    k -= 1
print(ans)
