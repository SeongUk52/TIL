import heapq

n = int(input())
q = []
total = 0
for i in range(n):
    heapq.heappush(q,int(input()))
while len(q)>=2:
    sum = heapq.heappop(q)
    sum += heapq.heappop(q)
    total+=sum
    heapq.heappush(q,sum)
print(total)