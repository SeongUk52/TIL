from collections import deque


def topology_sort():
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    ind = [0] * (n + 1)
    build_times = [0] * (n + 1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        ind[b] += 1
    goal = int(input())
    q = deque()
    for i in range(1, n + 1):
        if ind[i] == 0:
            if i == goal:
                print(d[i])
                return
            q.append(i)
    while q:
        now = q.popleft()
        if now == goal:
            break
        for i in graph[now]:
            build_times[i] = max(build_times[i], build_times[now] + d[now])
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)
    print(build_times[goal] + d[goal])


tc = int(input())
for _ in range(tc):
    topology_sort()
