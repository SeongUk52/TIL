import sys
input = sys.stdin.readline

def sorting(q,i,j):
    x = str(q[i])+str(q[j])
    y = str(q[j])+str(q[i])
    if x < y :
        temp = q[i]
        q[i] = q[j]
        q[j] = temp

k,n = map(int,input().split())
q = [int(input()) for i in range(k)]
q.sort()
for _ in range(n-k):
    q.append(q[-1])
for i in range(n-1):
    for j in range(i+1,n):
        sorting(q,i,j)
for i in q:
    print(i,end='')