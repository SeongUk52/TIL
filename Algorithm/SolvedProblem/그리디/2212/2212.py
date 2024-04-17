import heapq

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
lens = []
for i in range(n - 1):
    heapq.heappush(lens, arr[i] - arr[i + 1])

for i in range(k - 1):
    if lens:
        heapq.heappop(lens)
    else:
        break

print(-sum(lens))
