import heapq


def dijkstra():
    dists = {j:{i: float('infinity') for i in dict1} for j in range(k + 1)}
    for i in range(k + 1):
        dists[i][1] = 0
    q = [(0, 1, 0)]

    while q:
        cd, cv, ck = heapq.heappop(q)

        if cd > dists[ck][cv]:
            continue

        for nv, wt in dict1[cv].items():
            dist = max(cd, wt)
            if dist < dists[ck][nv]:
                for i in range(ck, k + 1):
                    if dists[i][nv] > dist:
                        dists[i][nv] = dist
                heapq.heappush(q, (dist, nv, ck))

        if ck < k:
            for nv in dict1[cv].keys():
                if cd < dists[ck + 1][nv]:
                    for i in range(ck + 1, k + 1):
                        if dists[i][nv] > cd:
                            dists[i][nv] = cd
                    heapq.heappush(q, (cd, nv, ck + 1))

    return dists


n, p, k = map(int, input().split())
dict1 = {i: {} for i in range(n + 1)}

for _ in range(p):
    a, b, c = map(int, input().split())
    dict1[a][b] = c
    dict1[b][a] = c
result = dijkstra()[k][n]
if result == float('infinity'):
    print(-1)
else:
    print(result)
