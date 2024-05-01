import heapq, sys
input = sys.stdin.readline

n, l = map(int, input().split())
hq = []

for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(hq, (a, b))

cnt = 0
tapeEnd = 0

while hq:
    a, b = heapq.heappop(hq)
    start = max(tapeEnd, a)
    insidePart = (b - start) // l
    if a >= tapeEnd:
        tapeEnd = start + l * max(1, insidePart)
        cnt += max(1, insidePart)

    if b > tapeEnd:
        heapq.heappush(hq, (tapeEnd, b))

print(cnt)
