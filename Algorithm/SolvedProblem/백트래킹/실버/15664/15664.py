def bt(st,comb):
    if len(comb) == m:
        if not comb in result:
            result.append(comb[:])
        return
    for i in range(st,n):
        comb.append(arr[i])
        bt(i + 1, comb)
        comb.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
result= []
arr.sort()
bt(0, [])
for i in result:
    print(*i)