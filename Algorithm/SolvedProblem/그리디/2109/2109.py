import heapq, sys
input = sys.stdin.readline

n = int(input())
md = 0
hq = []
result = 0
for i in range(n):
    p, d = map(int, input().split())
    if d > md:
        md = d
    heapq.heappush(hq, (-p, d))

assigned = [False] * (md + 1)

while hq:
    p, d = heapq.heappop(hq)
    p = - p
    for i in range(d, 0, - 1):
        if assigned[i]:
            continue
        assigned[i] = True
        result += p
        break

print(result)
