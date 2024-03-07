import sys
input = sys.stdin.readline

def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


n = int(input())
m = int(input())

arr = [i for i in range(n + 1)]

for i in range(n):
    ll = list(map(int, input().split()))
    for j in range(n):
        if ll[j] == 1:
            union(i + 1, j + 1)

ml = list(map(int, input().split()))
comp = arr[ml[0]]
result = "YES"

for i in ml:
    if comp != arr[i]:
        result = "NO"
        break

print(result)
