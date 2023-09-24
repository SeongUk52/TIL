def bt(comb):
    if len(comb) == m:
        result.append(comb[:])
        return
    for i in array:
        comb.append(i)
        bt(comb)
        comb.pop()

n, m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
result = []
bt([])
for i in result:
    print(*i)