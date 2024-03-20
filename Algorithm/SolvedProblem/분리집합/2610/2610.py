from collections import defaultdict
import sys

input = sys.stdin.readline
MAX = float('inf')

N = int(input())
M = int(input())
parent = list(range(N))
committee = defaultdict(list)


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    da = find(a)
    db = find(b)
    if da > db:
        parent[db] = da
    else:
        parent[da] = db


edge_list = [[MAX] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge_list[a][b] = edge_list[b][a] = 1
    union(a, b)

for k in range(N):
    dk = find(k)
    committee[dk].append(k)
    for i in range(N):
        for j in range(N):
            if edge_list[i][j] > edge_list[i][k] + edge_list[k][j]:
                edge_list[i][j] = edge_list[i][k] + edge_list[k][j]

answer = list()
for candidate in committee.values():
    result, result_val = 0, MAX
    for a in candidate:
        tmp_val = 0
        for b in candidate:
            if a == b:
                continue
            tmp_val = max(tmp_val, edge_list[a][b])
        if result_val > tmp_val:
            result, result_val = a, tmp_val
    answer.append(result + 1)
print(len(answer))
print(*sorted(answer), sep='\n')
