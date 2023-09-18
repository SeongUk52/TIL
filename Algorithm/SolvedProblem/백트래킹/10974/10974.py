def bt (n,comb,result):
    if len(comb) == n:
        result.append(comb[:])
        return
    for i in range(1,n+1):
        if i not in comb:
            comb.append(i)
            bt(n,comb,result)
            comb.pop()



n = int(input())
result = []
bt(n,[],result)
for i in result:
    print(*i,sep=' ')