from collections import deque


def bfs():
    q = deque()
    dists[a] = 0
    q.append((a, 0))
    while q:

        now, cnt = q.popleft()

        sur1 = now + 1
        if sur1 <= k and dists[sur1] > cnt + 1:
            dists[sur1] = cnt + 1
            q.append((sur1, cnt + 1))

        sur2 = now * 2
        if sur2 <= k and dists[sur2] > cnt + 1:
            dists[sur2] = cnt + 1
            q.append((sur2, cnt + 1))


a, k = map(int, input().split())

dists = [float('infinity')] * (k + 1)

bfs()

print(dists[-1])
