def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]


def union(a, b):
    rep1 = find(a)
    rep2 = find(b)
    arr[rep2] = rep1


n, m = map(int, input().split())

arr = [i for i in range(n + 1)]

for _ in range(m):
    cate, a, b = map(int,input().split())
    if cate == 0:
        union(a, b)
    if cate == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
