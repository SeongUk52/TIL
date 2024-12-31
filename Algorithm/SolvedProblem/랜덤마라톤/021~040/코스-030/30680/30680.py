import sys
from collections import defaultdict
import heapq

# 재귀 제한 늘리기
sys.setrecursionlimit(10**6)

def DFS(curr, depth, edge, visited, leaf_depth):
    count = 0
    for next_node in edge[curr]:
        if visited[next_node]:
            count += 1
            continue
        visited[next_node] = True
        DFS(next_node, depth + 1, edge, visited, leaf_depth)

    if len(edge[curr]) == count:
        leaf_depth.append(depth)

# 입력 처리 및 로직 실행
input = sys.stdin.read
data = input().split()
idx = 0

N = int(data[idx])
idx += 1
pq = [0]

for _ in range(N):
    A = int(data[idx])
    idx += 1

    leaf_depth = []
    edge = defaultdict(list)
    visited = [False] * (A + 1)

    for __ in range(A - 1):
        v, w = map(int, data[idx:idx+2])
        idx += 2
        edge[v].append(w)
        edge[w].append(v)

    visited[1] = True
    DFS(1, 0, edge, visited, leaf_depth)

    root_depth = heapq.heappop(pq)
    for depth in leaf_depth:
        heapq.heappush(pq, root_depth + depth + 1)

while True:
    answer = heapq.heappop(pq)
    if not pq:
        print(answer)
        break