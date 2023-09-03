import heapq

# 입력 받기
n, k = map(int, input().split())
jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))
bags = [int(input()) for _ in range(k)]

# 가방과 보석을 무게 오름차순으로 정렬
jewels.sort()
bags.sort()

total_value = 0
jewels_available = []  # 선택 가능한 보석을 저장할 우선순위 큐

jewel_index = 0
for bag in bags:
    # 현재 가방의 무게보다 가벼운 보석을 모두 우선순위 큐에 추가
    while jewel_index < n and jewels[jewel_index][0] <= bag:
        heapq.heappush(jewels_available, -jewels[jewel_index][1])  # 최대 힙을 위해 음수로 저장
        jewel_index += 1

    # 가장 가치가 높은 보석을 선택하여 누적 가치에 더함
    if jewels_available:
        total_value -= heapq.heappop(jewels_available)

print(total_value)