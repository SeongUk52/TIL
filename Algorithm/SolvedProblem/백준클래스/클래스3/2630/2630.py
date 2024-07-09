def recur(r0, r1, c0, c1):
    global cntw, cntb
    allw = True
    allb = True
    for i in range(r0, r1):
        if not allw and not allb:
            break
        for j in range(c0, c1):
            if graph[i][j] == 1:
                allw = False
            else:
                allb = False

    if allw:
        cntw += 1
    elif allb:
        cntb += 1
    else:
        midr = int((r0 + r1) / 2)
        midc = int((c0 + c1) / 2)
        recur(r0, midr, c0, midc)
        recur(r0, midr, midc, c1)
        recur(midr, r1, c0, midc)
        recur(midr, r1, midc, c1)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cntw = 0
cntb = 0
recur(0, n, 0, n)
print(cntw, cntb, sep="\n")
