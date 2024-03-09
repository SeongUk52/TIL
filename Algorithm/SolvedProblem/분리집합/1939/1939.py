import sys
input = sys.stdin.readline

def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]


def union(a, b):
    a, b = find(a), find(b)
    arr[max(a, b)] = min(a, b)


n, m = map(int, input().split())
arr = [i for i in range(n + 1)]
graph = []


for i in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort(reverse=True)

sf, ef = map(int, input().split())

for i in graph:
    c, a, b = i[0], i[1], i[2]
    union(a, b)
    if find(sf) == find(ef):
        print(c)
        break
