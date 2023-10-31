def bt(comb):
    if len(comb) == m:
        result.append(comb[:])
        return

    for i in arr:
        comb.append(i)
        bt(comb)
        comb.pop()


n, m = map(int,input().split())
arr = sorted(set(map(int, input().split())))
result = []
bt([])
for i in result:
    print(*i)