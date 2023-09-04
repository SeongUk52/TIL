import sys
input = sys.stdin.readline

def bt(n,q,comb,result):
    if len(comb) == n:
        tempInner = ''
        for i in comb:
            tempInner += str(q[i])
        if result[0] < int(tempInner):
            result[0] = int(tempInner)
    for i in range(0,n):
        if i not in comb:
            comb.append(i)
            bt(n,q,comb,result)
            comb.pop()


k,n = map(int,input().split())
q = [int(input()) for i in range(k)]
q.sort()
while len(q) <n:
    q.append(q[-1])
result = [0]
temp = 0
bt(n,q,[],result)
print(result[0])