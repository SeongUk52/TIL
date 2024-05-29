from collections import deque

t = int(input())
for _ in range(t):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    ind = [0] * (m + 1)
    strahler = [1] * (m + 1)
    inds = [{0: 0} for _ in range(m + 1)]
    q = deque()
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        ind[b] += 1

    for i in range(1, m + 1):
        if ind[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            ind[i] -= 1
            if strahler[now] in inds[i]:
                inds[i][strahler[now]] += 1
            else:
                inds[i][strahler[now]] = 1
            if ind[i] == 0:
                q.append(i)
                maxKey = max(inds[i].keys())
                if inds[i][maxKey] > 1:
                    strahler[i] = maxKey + 1
                else:
                    strahler[i] = maxKey

    print(k, strahler[m])
