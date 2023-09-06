import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
q = [deque() for i in range(min(n,m)//2)]
for i in range(min(n,m)//2):
    for j in range(i,m-i-1):
        q[i].append(a[i][j])
    for j in range(i,n-i-1):
        q[i].append(a[j][m-i-1])
    for j in range(i,m-i-1):
        q[i].append(a[n-i-1][m-j-1])
    for j in range(i,n-i-1):
        q[i].append(a[n-j-1][i])


for _ in range(r):
    for i in range(min(n,m)//2):
        q[i].append(q[i].popleft())

for i in range(min(n,m)//2):
    for j in range(i,m-i-1):
        a[i][j] = q[i].popleft()
    for j in range(i,n-i-1):
        a[j][m-i-1] = q[i].popleft()
    for j in range(i,m-i-1):
        a[n-i-1][m-j-1] = q[i].popleft()
    for j in range(i,n-i-1):
        a[n-j-1][i] = q[i].popleft()

for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()