import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    graph[A].append(B)
    graph[B].append(A)

def BFS(graph, start):
    num = [0] * (N + 1)
    ch[start] = 1
    Q = deque()
    Q.append(start)

    while Q:
        x = Q.popleft()
        for i in graph[x]:
            if ch[i] == 0:
                num[i] = num[x] + 1
                ch[i] = 1
                Q.append(i)

    return sum(num)


answer = []

for i in range(1, N + 1):
    ch = [0] * (N + 1)
    answer.append(BFS(graph, i))

print(answer.index(min(answer)) + 1)
