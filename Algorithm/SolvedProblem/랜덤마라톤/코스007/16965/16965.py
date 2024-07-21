from collections import deque


def bfs(a, b):
    visited = [False] * len(ranges)
    q = deque()
    q.append(a)
    visited[a] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                if i == b:
                    break

    return visited[b]


ranges = [None]
graph = [None]
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    if n == 1:
        ranges.append([x, y])
        graph.append([])
        for i in range(1, len(ranges)):
            if (ranges[i][0] < ranges[-1][0] < ranges[i][1]
                    or ranges[i][0] < ranges[-1][1] < ranges[i][1]):
                graph[-1].append(i)
            if (ranges[-1][0] < ranges[i][0] < ranges[-1][1]
                    or ranges[-1][0] < ranges[i][1] < ranges[-1][1]):
                graph[i].append(len(ranges) - 1)

    elif n == 2:
        if bfs(x, y):
            print(1)
        else:
            print(0)
