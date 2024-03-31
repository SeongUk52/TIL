n, m = map(int, input().split())

strs = [input() for _ in range(n)]
cnt = 0
result = ''

for j in range(m):
    cntEach = [0, 0, 0, 0]
    for i in range(n):
        if strs[i][j] == 'A':
            cntEach[0] += 1
        if strs[i][j] == 'C':
            cntEach[1] += 1
        if strs[i][j] == 'G':
            cntEach[2] += 1
        if strs[i][j] == 'T':
            cntEach[3] += 1
    idx = cntEach.index(max(cntEach))
    if idx == 0:
        result += 'A'
    if idx == 1:
        result += 'C'
    if idx == 2:
        result += 'G'
    if idx == 3:
        result += 'T'
    cnt += n - max(cntEach)

print(result)
print(cnt)
