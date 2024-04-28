import heapq, sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    hq = []
    result = 0
    for i in arr:
        heapq.heappush(hq, i)

    while len(hq) >= 2:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        result += a + b
        heapq.heappush(hq, a + b)
    print(result)
