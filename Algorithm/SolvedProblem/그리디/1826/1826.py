import sys
import heapq
input = sys.stdin.readline


n = int(input())
gs = []
q = []
for i in range(n):
    a,b = map(int,input().split())
    heapq.heappush(gs,(a,b))
l,p = map(int,input().split())
cnt = 0
while p < l:
    if gs:
        while gs[0][0] <= p:
            x,y = heapq.heappop(gs)
            heapq.heappush(q,(-y,x))
            if not gs:
                break
    if not q:
        cnt = -1
        break
    cnt += 1
    c = heapq.heappop(q)
    p += -c[0]
print(cnt)