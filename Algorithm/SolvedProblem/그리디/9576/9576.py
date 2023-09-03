import sys

def dfs(x,ll,d,c):
    a = ll[x-1][0]
    b = ll[x-1][1]
    for i in range(a,b+1):
        if c[i]:
            continue
        c[i] = True
        if d[i] == 0 or dfs(d[i], ll, d,c):
            d[i] = x
            return True

    return False

t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    d = [0]*(n+1)
    cnt = 0
    ll = [list(map(int,input().split())) for i in range(m)]
    for i in range(1,m+1):
        c = [False]*(n+1)
        if dfs(i,ll,d,c):
            cnt += 1
    print(cnt)
