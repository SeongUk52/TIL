import sys

input = sys.stdin.readline


def find(n):
    if n != arr[n]:
        arr[n] = find(arr[n])
    return arr[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


n, m = map(int, input().split())
arr = [i for i in range(n)]

result = 0

for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        result = i + 1
        break

    union(a, b)

print(result)
