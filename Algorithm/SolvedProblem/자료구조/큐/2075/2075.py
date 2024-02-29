import heapq
q = []
n = int(input())

for i in range(n):
    ll = list(map(int, input().split()))
    for j in ll:
        if len(q) < n:
            heapq.heappush(q, j)
        else:
            if q[0] < j:
                heapq.heappop(q)
                heapq.heappush(q, j)

print(q[0])
