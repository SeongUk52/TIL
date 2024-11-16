import heapq

for _ in range(int(input())):
    j, n = map(int, input().split())
    hq = [-a * b for a, b in [map(int, input().split()) for _ in range(n)]]
    heapq.heapify(hq)

    for cnt in range(1, n + 1):
        j += heapq.heappop(hq)
        if j <= 0:
            print(cnt)
            break
