def find(u):
    if p[u] < 0:
        return u

    p[u] = find(p[u])
    return p[u]


def union(u, v):
    u, v = find(u), find(v)

    if u == v:
        return

    p[v] = u


G, P = int(input()), int(input())
p = [-1 for i in range(G + 1)]
ans = 0
for i in range(P):
    g = int(input())
    target = find(g)
    if target == 0:
        break
    union(target - 1, target)
    ans += 1

print(ans)
