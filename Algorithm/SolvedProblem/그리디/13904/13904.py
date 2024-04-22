import heapq, sys
input = sys.stdin.readline

n = int(input())
hq = []
md = 0
for i in range(n):
    d, w = map(int, input().split())
    heapq.heappush(hq, (-w, d))
    if md < d:
        md = d

assigned = [False] * (md + 1)

result = 0
while hq:
    w, d = heapq.heappop(hq)
    w = - w
    for i in range(d, 0, - 1):
        if assigned[i]:
            continue

        assigned[i] = True
        result += w
        break

print(result)
