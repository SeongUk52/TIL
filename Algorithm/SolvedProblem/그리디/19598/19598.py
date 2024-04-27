import heapq, sys
input = sys.stdin.readline

n = int(input())
hq = []

for i in range(n):
    start, end = map(int, input().split())
    heapq.heappush(hq, (start, end))

rooms = [0]
while hq:
    start, end = heapq.heappop(hq)
    flag = True

    for i in range(len(rooms)):
        if start >= rooms[i]:
            rooms[i] = end
            flag = False
            break

    if flag:
        rooms.append(end)

print(len(rooms))
