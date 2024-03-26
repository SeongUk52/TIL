import heapq

n = int(input())
dasom = int(input())
cnt = 0
candies = []

for i in range(n - 1):
    heapq.heappush(candies, -int(input()))


while candies:
    maxi = -heapq.heappop(candies)
    if dasom > maxi:
        break

    dasom += 1
    cnt += 1
    heapq.heappush(candies, - (maxi - 1))

print(cnt)
