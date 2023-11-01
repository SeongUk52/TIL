import heapq


def dijkstra():
    dists = {i: float('infinity') for i in dict1}
    dists[1] = 0
    q = [(0, 1, k)]

    while q:
        cd, cv, ck = heapq.heappop(q)

        if cd > dists[cv]:
            continue

        for nv, wt in dict1[cv].items():
            dist = max(cd, wt)
            if dist < dists[nv]:
                dists[nv] = dist
                heapq.heappush(q, (dist, nv, k))

        if ck > 0:
            for nv, wt in dict1[cv].items():
                if cd < dists[nv]:
                    dists[nv] = cd
                    heapq.heappush(q, (cd, nv, k - 1))

    return dists


n, p, k = map(int, input().split())
dict1 = {i: {} for i in range(n + 1)}

for _ in range(p):
    a, b, c = map(int, input().split())
    dict1[a][b] = c
    dict1[b][a] = c

print(dict1)
result = dijkstra()
if result == float('infinity'):
    print(-1)
else:
    print(result)
