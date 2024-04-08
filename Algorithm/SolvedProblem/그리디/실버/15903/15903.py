import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)

for _ in range(m):
    temp = heapq.heappop(arr)
    temp += heapq.heappop(arr)
    heapq.heappush(arr, temp)
    heapq.heappush(arr, temp)

print(sum(arr))
