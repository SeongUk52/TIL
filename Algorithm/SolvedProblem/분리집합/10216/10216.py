import math
import sys
input = sys.stdin.readline


def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


for _ in range(int(input())):
    n = int(input())
    arr = [i for i in range(n + 1)]
    graph = [[0,0,0]]
    for i in range(n):
        x, y, r = map(int, input().split())
        graph.append([x, y, r])

    for i in range(1, n):
        x1, y1, r1 = graph[i]
        for j in range(i, n + 1):
            if find(i) == find(j):
                continue
            x2, y2, r2 = graph[j]
            if r1 + r2 >= math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2):
                union(i, j)

    result = 0

    for i in range(1, n + 1):
        if arr[i] == i:
            result += 1
    print(result)
